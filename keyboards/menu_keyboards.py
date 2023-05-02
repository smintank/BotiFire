from typing import Optional

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.menu_buttons import SERVICE_BTN


def get_keyboard(buttons: dict[str :str],
                 last_btn: Optional[list[str]] = None,
                 wight: int = 1
                 ) -> InlineKeyboardMarkup:
    """Make inline keyboard from dict"""
    builder = InlineKeyboardBuilder()
    count = 0
    for callback, text in buttons.items():
        if count % wight == 0:
            builder.row(InlineKeyboardButton(text=text, callback_data=callback))
        else:
            builder.add(InlineKeyboardButton(text=text, callback_data=callback))
        count += 1
    if last_btn:
        for callback in last_btn:
            builder.row(InlineKeyboardButton(text=SERVICE_BTN[callback], callback_data=callback))
    return builder.as_markup()

