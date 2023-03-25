from sqlite3 import Cursor
from typing import Any

from aiogram.types import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

import db


"""Main inline menu"""
inline_shift_notify: InlineKeyboardButton = InlineKeyboardButton('📩 Смена на завтра', callback_data='shift_notify')
inline_notify: InlineKeyboardButton = InlineKeyboardButton('📥 Оповестить ...', callback_data='notify')
inline_replace: InlineKeyboardButton = InlineKeyboardButton('🔁 Замена', callback_data='replace_person')
inline_status: InlineKeyboardButton = InlineKeyboardButton('ℹ️ Статус', callback_data='notify_status')

main_inline_menu: InlineKeyboardMarkup = InlineKeyboardMarkup()
main_inline_menu.row(inline_shift_notify)
main_inline_menu.row(inline_notify)
main_inline_menu.row(inline_replace)
main_inline_menu.row(inline_status)


def post_markup():
    """Post choosing inline menu"""
    post_inline_menu: InlineKeyboardMarkup = InlineKeyboardMarkup()
    cursor: Cursor = db.get_cursor()
    cursor.execute("SELECT alias, name FROM post WHERE is_main=TRUE")
    result: list[Any] = cursor.fetchall()
    for post_alias, post_name in result:
        post_inline_menu.row(InlineKeyboardButton(f'{post_alias}', callback_data=f'post_{post_name}'))
    post_inline_menu.row(InlineKeyboardButton(f'...', callback_data='post_ets'))
    return post_inline_menu


"""Ok and Cancel inline keyboard"""
inline_ok: InlineKeyboardButton = InlineKeyboardButton('✅ ОК', callback_data='ok_btn')
inline_deny: InlineKeyboardButton = InlineKeyboardButton('Не ОК! 🟥', callback_data='deny_btn')
agree_inline_menu: InlineKeyboardMarkup = InlineKeyboardMarkup()
agree_inline_menu.add(inline_ok, inline_deny)


"""Remove keyboard"""
remove_menu: ReplyKeyboardRemove = ReplyKeyboardRemove()
