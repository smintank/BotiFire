import logging
import os
from aiogram import Bot, Dispatcher, executor, types

from middlewares import AccessMiddleware
from constants import START_MESSAGE, HELP_MESSAGE
import markup as menu
import shifts

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv("TG_API"))
dp = Dispatcher(bot)
dp.middleware.setup(AccessMiddleware())


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(START_MESSAGE)


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply(HELP_MESSAGE)


@dp.message_handler(commands=['menu'])
async def send_welcome(message: types.Message):
    await message.answer("Что вы хотите сделать?", reply_markup=menu.main_inline_menu)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


@dp.callback_query_handler(text="shift_notify")
async def process_callback_notify(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Ведите фамилию и пост')
    await bot.send_message(callback_query.from_user.id, str(shifts.create_shift()))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
