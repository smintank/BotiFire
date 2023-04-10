from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.menu_buttons import SERVICE_BTN


def get_keyboard(buttons: dict[str: str],
                 last_btn: str | None = None,
                 width: int = 1
                 ) -> InlineKeyboardMarkup:
    """Make inline keyboard from dict"""
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.row(*_get_buttons(buttons, last_btn), width=width)
    return keyboard_builder.as_markup()


def _get_buttons(buttons: dict[str: str],
                 last_btn: str | None = None
                 ) -> list[InlineKeyboardButton]:
    """Append buttons to list"""
    markup: list = [InlineKeyboardButton(text=text, callback_data=button) for button, text in buttons.items()]
    if last_btn:
        markup.append(InlineKeyboardButton(text=SERVICE_BTN[last_btn], callback_data=last_btn))
    return markup


