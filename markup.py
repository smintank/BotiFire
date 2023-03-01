from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

btn_main_menu = KeyboardButton('⬅️ Главное меню')

btn_notify = KeyboardButton('📩 Оповестить')
btn_replace = KeyboardButton('🔁 Замена')

main_menu = ReplyKeyboardMarkup().add(btn_replace, btn_notify)
