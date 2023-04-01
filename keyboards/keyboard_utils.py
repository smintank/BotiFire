from sqlite3 import Cursor
from typing import Any

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import db


def posts_inline_keyboard() -> InlineKeyboardMarkup:
    """Post choosing inline menu"""
    cursor: Cursor = db.get_cursor()
    cursor.execute("SELECT alias, name FROM post WHERE is_main=TRUE")
    result: list[Any] = cursor.fetchall()
    keyboard_buttons = []
    for post_alias, post_name in result:
        button = [InlineKeyboardButton(f'{post_alias}', callback_data=f'post_{post_name}')]
        keyboard_buttons.append(button)
    etc_button = [InlineKeyboardButton(f'...', callback_data='post_ets')]
    keyboard_buttons.append(etc_button)
    return InlineKeyboardMarkup(inline_keyboard_markup=keyboard_buttons)
