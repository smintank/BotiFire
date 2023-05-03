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
    _make_buttons(builder, buttons, wight)

    if last_btn:
        service_buttons = {btn: SERVICE_BTN[btn] for btn in last_btn}
        _make_buttons(builder, service_buttons, 3)
    return builder.as_markup()


def _make_buttons(
        builder: InlineKeyboardBuilder,
        buttons: dict[str: str],
        wight: int=1
) -> InlineKeyboardBuilder:
    count = 0
    for callback, text in buttons.items():
        button = InlineKeyboardButton(text=text, callback_data=callback)
        if count % wight == 0:
            builder.row(button)
        else:
            builder.add(button)
        count += 1
    return builder


def get_service_keyboard(buttons: list[str]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for button in buttons:
        builder.add(InlineKeyboardButton(text=SERVICE_BTN[button], callback_data=button))
    return builder.as_markup()