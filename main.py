import logging
import os

import asyncio
from aiogram import Bot, Dispatcher, executor, types

from middlewares import AccessMiddleware

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv("TG_API"))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    user_id = str(message.from_user)
    await message.reply(f"Привет {user_id}, я помогу тебе отправить оповещения. \n"
                        f"Выбери вариант оповещения, нажав на одну из кнопок меню.")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)
