from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


"""Main inline menu"""
inline_shift_notify: InlineKeyboardButton = InlineKeyboardButton(text='📩 Смена на завтра', callback_data='shift_notify')
inline_notify: InlineKeyboardButton = InlineKeyboardButton(text='📥 Оповестить ...', callback_data='notify')
inline_replace: InlineKeyboardButton = InlineKeyboardButton(text='🔁 Замена', callback_data='replace_person')
inline_status: InlineKeyboardButton = InlineKeyboardButton(text='ℹ️ Статус', callback_data='notify_status')

main_inline_menu: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard_markup=[[inline_shift_notify],
                                                                                      [inline_notify],
                                                                                      [inline_replace],
                                                                                      [inline_status]
                                                                                      ])
