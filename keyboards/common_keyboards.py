from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


"""Ok and Cancel inline keyboard"""
inline_ok: InlineKeyboardButton = InlineKeyboardButton('✅ ОК', callback_data='ok_btn')
inline_deny: InlineKeyboardButton = InlineKeyboardButton('Не ОК! 🟥', callback_data='deny_btn')
agree_inline_menu: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard_markup=[[inline_ok, inline_deny]])
