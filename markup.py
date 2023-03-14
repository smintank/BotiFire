from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

import db

btn_main_menu = KeyboardButton('⬅️ Главное меню')

btn_shift_notify = KeyboardButton('📩 Оповестить смену')
btn_notify = KeyboardButton('📥 Оповестить ...')
btn_replace = KeyboardButton('🔁 Замена')

main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_shift_notify, btn_replace, btn_notify)


inline_shift_notify = InlineKeyboardButton('📩 Смена на завтра', callback_data='shift_notify')
inline_notify = InlineKeyboardButton('📥 Оповестить ...', callback_data='notify')
inline_replace = InlineKeyboardButton('🔁 Замена', callback_data='replace_person')
inline_status = InlineKeyboardButton('ℹ️ Статус', callback_data='notify_status')


main_inline_menu = InlineKeyboardMarkup()
main_inline_menu.row(inline_shift_notify)
main_inline_menu.row(inline_notify)
main_inline_menu.row(inline_replace)
main_inline_menu.row(inline_status)


def post_markup():
    post_inline_menu = InlineKeyboardMarkup()
    cursor = db.get_cursor()
    cursor.execute("SELECT name FROM post")
    result = cursor.fetchall()
    for post_name in result:
        post_inline_menu.row(InlineKeyboardButton(f'{post_name}', callback_data=f'post_{post_name}'))
    return post_inline_menu


inline_ok = InlineKeyboardButton('✅ ОК', callback_data='ok_btn')
inline_deny = InlineKeyboardButton('Не ОК! 🟥', callback_data='deny_btn')

agree_inline_menu = InlineKeyboardMarkup()
agree_inline_menu.add(inline_ok, inline_deny)

remove_menu = ReplyKeyboardRemove()
