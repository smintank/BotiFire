from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup

from lexicon import lexicon_ru, menu_buttons
from keyboards import menu_keyboards
from model.methods import posts_employee_process, get_shift, shift
import model.models as shifts


router: Router = Router()


@router.message(Command(commands=['start']))
async def send_welcome(message: Message) -> None:
    """Handler for 'start' command in telegram"""
    await message.reply(lexicon_ru.START_MESSAGE)


@router.message(Command(commands=['help']))
async def send_help(message: Message) -> None:
    """Handler for 'help' command in telegram"""
    await message.reply(lexicon_ru.HELP_MESSAGE)


@router.message(Command(commands=['menu']))
async def send_menu(message: Message) -> None:
    """Handler for 'menu' command in telegram"""
    keyboard = menu_keyboards.get_keyboard(menu_buttons.main_inline_menu, width=1)
    await message.answer("Что вы хотите сделать?", reply_markup=keyboard)


@router.callback_query(Text(text="notify"))
async def process_callback_notify(callback: CallbackQuery) -> None:
    """Callback handler for shift notify menu button"""
    await callback.message.edit_text(text=menu_buttons.CHOSE_POST,
                                     reply_markup=get_shift())


@router.callback_query(lambda c: c.data and c.data in shift.posts)
async def process_callback_posts(callback: CallbackQuery) -> None:
    """Callback handler for post choosing menu buttons"""
    print('Отработал хендлер с лябдой')
    post = callback.data
    print(post)
    await callback.message.edit_text(text=menu_buttons.CHOSE_EMPLOYEE,
                                     reply_markup=posts_employee_process(post))


@router.callback_query(Text(text="ok_btn"))
async def process_callback_ok(callback: CallbackQuery):
    """Callback handler for handle 'Ok' button pressing"""
    shifts.new_shift.agreed = callback.id
    await callback.answer('✅🪖🔫')


@router.callback_query(Text(text="deny_btn"))
async def process_callback_deny(callback: CallbackQuery):
    """Callback handler for handle 'Cancel' button pressing"""
    await callback.answer('Укажите причину:')
