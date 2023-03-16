import logging
import os
from aiogram import Bot, Dispatcher, executor, types

from middlewares import AccessMiddleware
from defaults import START_MESSAGE, HELP_MESSAGE
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
async def send_menu(message: types.Message):
    await message.answer("Что вы хотите сделать?", reply_markup=menu.main_inline_menu)


@dp.message_handler()
async def send_text(message: types.Message):
    shifts.new_shift.add_shift(message.text, message.from_user.id)
    await message.answer('Выберете пост:', reply_markup=menu.post_markup())


@dp.callback_query_handler(text="shift_notify")
async def process_callback_notify(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Ведите фамилию сотрудника:', reply_markup=menu.remove_menu)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('post_'))
async def process_callback_posts(callback_query: types.CallbackQuery):
    post = callback_query.data[5:]
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f'Нажата кнопка "{post}"', reply_markup=menu.remove_menu)
    # await bot.send_message(callback_query.from_user.id,
    #                           'Ведите фамилию следующего сотрудника:', reply_markup=menu.remove_menu)


@dp.callback_query_handler(text="ok_btn")
async def process_callback_ok(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    shifts.new_shift.agreed = callback_query.id
    await bot.send_message(callback_query.from_user.id, '✅🪖🔫', reply_markup=menu.remove_menu)


@dp.callback_query_handler(text="deny_btn")
async def process_callback_deny(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Укажите причину:', reply_markup=menu.remove_menu)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
