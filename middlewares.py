from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware


class AccessMiddleware(BaseMiddleware):
    def __init__(self, access_id):
        self.access_id = access_id
        super().__init__()

    def on_process_message(self, message: types.Message, _):
        pass
