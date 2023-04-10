from aiogram import Router
from aiogram.types import Message

router: Router = Router()


@router.message()
async def echo_message(message: Message) -> None:
    """Handler for rest of messages"""
    await message.answer(message.text)
