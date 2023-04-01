from aiogram import Router
from aiogram.types import Message

import shifts
from keyboards.keyboard_utils import posts_inline_keyboard

router: Router = Router()


@router.message()
async def send_text(message: Message) -> None:
    """Handler for rest of messages"""
    shifts.new_shift.add_shift(message.text, str(message.from_user.id))
    await message.answer('Выберете пост:', reply_markup=posts_inline_keyboard())
