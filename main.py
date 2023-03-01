import logging
import os
from aiogram import Bot, Dispatcher, executor, types

from middlewares import AccessMiddleware
from constants import START_MESSAGE, HELP_MESSAGE
import markup as nav

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv("TG_API"))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(START_MESSAGE)


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply(HELP_MESSAGE)


@dp.message_handler(commands=['menu'])
async def send_welcome(message: types.Message):
    await message.answer("Что вы хотите сделать?", reply_markup=nav.main_menu)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
