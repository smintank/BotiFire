from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

btn_main_menu = KeyboardButton('⬅️ Главное меню')

btn_shift_notify = KeyboardButton('📩 Оповестить смену')
btn_notify = KeyboardButton('📥 Оповестить ...')
btn_replace = KeyboardButton('🔁 Замена')

main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_shift_notify, btn_replace, btn_notify)


inline_shift_notify = InlineKeyboardButton('📩 Оповестить смену', callback_data='shift_notify')
inline_notify = InlineKeyboardButton('📥 Оповестить ...', callback_data='notify')
inline_replace = InlineKeyboardButton('🔁 Замена', callback_data='replace_person')


main_inline_menu = InlineKeyboardMarkup()
main_inline_menu.row(inline_shift_notify)
main_inline_menu.row(inline_notify)
main_inline_menu.row(inline_replace)
