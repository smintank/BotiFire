from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message

from lexicon import lexicon_ru, menu_buttons
from keyboards import menu_keyboards


router: Router = Router()

@router.message(Command(commands=['start']), StateFilter(default_state))
async def send_welcome(message: Message) -> None:
    """Handler for 'start' command in telegram"""
    await message.reply(lexicon_ru.START_MESSAGE)


@router.message(Command(commands=['help']), StateFilter(default_state))
async def send_help(message: Message) -> None:
    """Handler for 'help' command in telegram"""
    await message.reply(lexicon_ru.HELP_MESSAGE)


@router.message(Command(commands=['menu']), StateFilter(default_state))
async def send_menu(message: Message) -> None:
    """Handler for 'menu' command in telegram"""
    keyboard = menu_keyboards.get_keyboard(menu_buttons.MAIN_INLINE_MENU)
    await message.answer("Что вы хотите сделать?", reply_markup=keyboard)
