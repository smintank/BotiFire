import datetime as dt
from typing import NamedTuple
import re

import defaults
import exceptions
import db
import main
import markup as menu


class NewShifts(NamedTuple):
    date: str
    post_id: int
    person_tg_id: str
    creator: str


class Shift:
    def __init__(self):
        self.shifts_date = None
        self.today_date = None
        self.post_id = 0
        self.post_name = ''
        self.person_tg_id = 0
        self.creator_tg_id = ''
        self.notified = []
        self.agreed = []

    def add_shift(self, message: str, creator_tg_id: str):
        self.today_date = dt.datetime.today()
        self.shifts_date = dt.date.today() + dt.timedelta(days=1)
        self.creator_tg_id = creator_tg_id
        parsed_person = parse_message(message)  # Парсинг сообщения на поиск фамилии
        shift_item = self._validate_data(parsed_person)  # Проверка существует ли такой пользователь в БД
        self.person_tg_id = shift_item[0]
        self.notify(self.person_tg_id, self.post_name)
        self.notified.append(shift_item)  # Добавление в отслеживание статуса оповещения


    def set_post(self, post_id: int):
        self.post_id = post_id

    def _validate_data(self, parsed_person: [str]) -> [str]:
        cursor = db.get_cursor()
        cursor.execute(f"SELECT id, last_name, first_name, mid_name FROM person WHERE last_name='{parsed_person[0]}' ")
        db_results = cursor.fetchall()
        if db_results is None or not db_results:
            raise exceptions.NotCorrectMessage(defaults.NAME_CHECK_ERROR_MESSAGE)

        name = ' '.join(parsed_person)
        count = len(parsed_person)
        match = []
        for result in db_results:
            join_result = ''
            for index in range(count):
                str_len = len(parsed_person[index])
                join_result += result[index + 1][:str_len] + ' '
            if name == join_result[:-1]:
                match.append(result)
        if match and len(match) == 1:
            return match[0]
        else:
            raise exceptions.NotCorrectMessage(defaults.SURNAME_CHECK_ERROR_MESSAGE)

    def notify(self, person_tg_id: int, post_name: str):
        main.bot.send_message(str(person_tg_id),
                              text=f'Ты заступаешь завтра: {post_name}', reply_markup=menu.agree_inline_menu)


def parse_message(text: str) -> [str]:
    text = to_ru_letters(text.lower())
    parsed_text = re.search(r'(\b[а-яё]{2,20}\b ?[а-я]?\.? ?[а-я]?\.?)', text)
    if parsed_text is None or not parsed_text.group(0):
        raise exceptions.NotCorrectMessage(defaults.NAME_CHECK_ERROR_MESSAGE)
    person_name = parsed_text.group(0).lower().replace('ё', 'е')
    return person_name.replace('.', ' ').split()


def to_ru_letters(word: str) -> str:
    letters = {'en': 'abcehkmoptuxy', 'ru': 'авсенкмортиху'}
    result = ''
    for letter in word:
        if letter in letters['en']:
            index = letters['en'].index(letter)
            result += letters['ru'][index]
        else:
            result += letter
    return result


new_shift = Shift()


if __name__ == '__main__':
    shift = Shift()
    shift.add_shift('Смaгин Д.A.', '220697264')
