from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

import lexicon.lexicon_ru
from keyboards import menu_keyboards
import shifts

router: Router = Router()


@router.message(CommandStart)
async def send_welcome(message: Message) -> None:
    """Handler for 'start' command in telegram"""
    await message.reply(lexicon.lexicon_ru.START_MESSAGE)


@router.message(commands=['help'])
async def send_welcome(message: Message) -> None:
    """Handler for 'help' command in telegram"""
    await message.reply(lexicon.lexicon_ru.HELP_MESSAGE)


@router.message(commands=['menu'])
async def send_menu(message: Message) -> None:
    """Handler for 'menu' command in telegram"""
    await message.answer("Что вы хотите сделать?", reply_markup=menu_keyboards.main_inline_menu)


@router.callback_query(text="shift_notify")
async def process_callback_notify(callback: CallbackQuery) -> None:
    """Callback handler for shift notify menu button"""
    await callback.answer('Ведите фамилию сотрудника:')


@router.callback_query(lambda c: c.data and c.data.startswith('post_'))
async def process_callback_posts(callback: CallbackQuery) -> None:
    """Callback handler for post choosing menu buttons"""
    post = callback.data[5:]
    await callback.answer(f'Нажата кнопка "{post}"')
    await callback.answer('Ведите фамилию следующего сотрудника:')


@router.callback_query(text="ok_btn")
async def process_callback_ok(callback: CallbackQuery):
    """Callback handler for handle 'Ok' button pressing"""
    shifts.new_shift.agreed = callback.id
    await callback.answer('✅🪖🔫')


@router.callback_query(text="deny_btn")
async def process_callback_deny(callback: CallbackQuery):
    """Callback handler for handle 'Cancel' button pressing"""
    await callback.answer('Укажите причину:')
