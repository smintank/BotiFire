from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
import db


class AccessMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()

    async def on_process_message(self, message: types.Message, _):
        if str(message.from_user.id) not in self._get_list():
            await message.answer("Access Denied")
            raise CancelHandler()

    def _get_list(self):
        cursor = db.get_cursor()
        cursor.execute("SELECT id FROM person")
        result = cursor.fetchall()
        return result[0]
