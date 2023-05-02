from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.state import default_state
from aiogram.filters import StateFilter

router: Router = Router()


@router.message(StateFilter(default_state))
async def echo_message(message: Message) -> None:
    """Handler for rest of messages"""
    await message.answer(message.text)
