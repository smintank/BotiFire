"""Кастомное исключение, генерируемое приложением"""


class NotCorrectMessage(Exception):
    """Некорректное сообщение в бот, которое не удалось распарсить или распознать"""
    pass