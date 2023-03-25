from main import bot


def send_message(tg_id: str, text: str, keyboard=None) -> None:
    """Send message in telegram"""
    bot.send_message(tg_id, text=text, reply_markup=keyboard)
