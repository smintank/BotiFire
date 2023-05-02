import logging

from aiogram.dispatcher.router import Router
from aiogram.filters import Text, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.types import CallbackQuery, Message

from keyboards import menu_keyboards
from keyboards.menu_keyboards import get_keyboard
from model.methods import get_shift, get_employees, shifts, employees, set_shift
from lexicon import menu_buttons

router: Router = Router()


class FSMNotificationData(StatesGroup):
    fill_post = State()
    fill_name = State()
    fill_message = State()
    fill_date = State()
    send_msgs = State()


@router.callback_query(Text(text="notify"), StateFilter(default_state))
async def process_callback_notify(callback: CallbackQuery, state: FSMContext) -> None:
    """Callback handler for shift notify menu button"""
    inline_markup = get_keyboard(get_shift(), last_btn=['cancel'])
    await callback.message.edit_text(text=menu_buttons.CHOSE_POST,
                                     reply_markup=inline_markup)
    await state.set_state(FSMNotificationData.fill_post)
    logging.info('Current state: fill_post')


@router.callback_query(lambda c: c.data and c.data in shifts.keys(),
                       StateFilter(FSMNotificationData.fill_post))
async def process_callback_posts(callback: CallbackQuery, state: FSMContext) -> None:
    """Callback handler for post choosing"""
    await state.update_data(post=callback.data)
    inline_markup = get_keyboard(get_employees(), last_btn=['cancel'], wight=2)
    await callback.message.edit_text(text=menu_buttons.CHOSE_EMPLOYEE,
                                     reply_markup=inline_markup)
    await state.set_state(FSMNotificationData.fill_name)
    logging.info('Current state: fill_name')


@router.callback_query(lambda c: c.data and c.data == 'cancel',
                       ~StateFilter(default_state))
async def cancel_state(callback: CallbackQuery, state: FSMContext) -> None:
    inline_markup = menu_keyboards.get_keyboard(menu_buttons.MAIN_INLINE_MENU)
    await callback.message.edit_text(text="Что вы хотите сделать?", reply_markup=inline_markup)
    await state.clear()


@router.message(StateFilter(FSMNotificationData.fill_post))
async def warning_not_name(message: Message):
    """Warning message is shown if the bot is in the fill_post state
    and a user trying to do something instead of choosing a post"""
    await message.answer(text=menu_buttons.NOT_POST_MSG)


@router.callback_query(lambda c: c.data and c.data in employees,
                       StateFilter(FSMNotificationData.fill_name))
async def process_callback_names(callback: CallbackQuery, state: FSMContext) -> None:
    """Callback handler for employee choosing"""
    await state.update_data(employee=callback.data)
    set_shift(await state.get_data(), str(callback.from_user.id))
    await state.set_state(FSMNotificationData.fill_post)
    inline_markup = get_keyboard(get_shift(), last_btn=['clear', 'notify'])
    await callback.message.edit_text(text=menu_buttons.CHOSE_POST,
                                     reply_markup=inline_markup)
    logging.info('Current state: fill_post')


@router.message(StateFilter(FSMNotificationData.fill_name))
async def warning_not_name(message: Message):
    """Warning message is shown if the bot is in the fill_name state
    and a user trying to do something instead of choosing an employee"""
    await message.answer(text=menu_buttons.NOT_NAME_MSG)