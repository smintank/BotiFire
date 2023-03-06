from typing import NamedTuple
import re

import defaults
import exceptions


class NewShifts(NamedTuple):
    date: str
    post: str
    person: str
    creator: str


class Shift:
    def __init__(self):
        self.date = ''
        self.shift = ''
        self.creator = ''

    def add_shift(self, message: str, creator_id: str):
        self.creator = creator_id
        parsed_dict = parse_message(message)
        if self.data_match(parsed_dict):
            # TODO: Записать id провалидированных данных в Именованный кортеж и записать всё в базу
            # TODO: Добавить в словарь id о том что ожидает подтверждения от оповещаемого

    # def _validate(self, tg_id: str) -> bool:
    #     if self.creator == tg_id:
    #         return True
    #     else:
    #         return False

    def data_match(self, parsed_dict: dict) -> bool:
        pass
    # TODO: Написать проверку в базе на соответствие переданным данным


def parse_message(text: str) -> dict:
    parsed_text = re.search(r'(\b[А-ЯЁ]?[а-яё]{4,20}\b ?[А-Яа-я]?\.?)[- ]{1,3}(.+)', text)

    if parsed_text is None or not parsed_text.group(0) or not parsed_text.group(1) or not parsed_text.group(2):
        raise exceptions.NotCorrectMessage(defaults.PARSE_ERROR_MESSAGE)

    employee_name = parsed_text.group(1).lower().replace('ё', 'е')
    post_name = parsed_text.group(2).lower().replace(' ', '')

    return {employee_name: post_name}


new_shift = Shift()
