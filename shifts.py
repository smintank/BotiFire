from typing import NamedTuple
import re

import defaults
import exceptions
import db


class NewShifts(NamedTuple):
    date: str
    post_id: int
    person: str
    creator: str


class Shift:
    def __init__(self):
        self.date = ''
        self.post_id = 0
        self.person = ''
        self.creator = ''
        self.notified = []
        self.agreed = []

    def add_shift(self, message: str, creator_id: str):
        self.creator = creator_id
        parsed_person = parse_message(message)          # Парсинг сообщения на поиск фамилии
        shift = self._validate_data(parsed_person)      # Проверка существует ли такой пользователь в БД
        self.notified.append(shift)                     # Добавление в отслеживание статуса оповещения
        # db.insert('day_post_user',                      # Добавление данных в БД
        #           {
        #               'workday_id': shift.date,
        #               'post_id': shift.post_id,
        #               'person_id': shift.person,
        #               'creator_id': shift.creator
        #           })
        return f'{shift.person} пользователь добавлен на пост {shift.post_id} на дату {shift.date}'

    def set_post(self, post_id: int):
        self.post_id = post_id

    def _validate_data(self, parsed_person: [str]) -> NewShifts:
        last_name = parsed_person[0].lower()
        persons = db.fetchall('person', ['id', 'first_name', 'last_name'])
        matches = []
        result = {}
        for person in persons:
            if last_name == person['last_name'].lower():
                matches.append(person)
        if len(matches) == 1:
            result = matches[0]
        elif len(matches) > 1:
            for match in matches:
                if parsed_person[1][1].lower() == match.first_name[1].lower():
                    result = match
        else:
            raise exceptions.NotCorrectMessage(defaults.NAME_CHECK_ERROR_MESSAGE)

        if result:
            self.person = result['id']
            return NewShifts(
                date=self.date,
                post_id=self.post_id,
                person=self.person,
                creator=self.creator
            )


def parse_message(text: str) -> [str]:
    parsed_text = re.search(r'(\b[А-ЯЁ]?[а-яё]{4,20}\b ?[А-Яа-я]?\.?)', text)

    if parsed_text is None or not parsed_text.group(0) or not parsed_text.group(1):
        raise exceptions.NotCorrectMessage(defaults.PARSE_ERROR_MESSAGE)

    person_name = parsed_text.group(1).lower().replace('ё', 'е')
    person = person_name.replace('.', '').split()

    return person


new_shift = Shift()
