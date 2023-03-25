import datetime as dt
from typing import NamedTuple, Optional, Match
import re

import sender
import settings
import exceptions
import db
import markup


class NewShifts(NamedTuple):
    date: str
    post_id: int
    person_tg_id: str
    creator: str


class Shift:
    """Shift-post entity"""

    def __init__(self):
        self.shifts_date = None
        self.today_date = None
        self.post_id = 0
        self.post_name = ''
        self.person_tg_id = 0
        self.creator_tg_id = ''
        self.notified = []
        self.agreed = []

    def add_shift(self, message: str, creator_tg_id: str) -> None:
        """Process of shift creation"""

        parsed_person = parse_message(message)      # Parse the massage to find employee credentials
        shift_item = validate_data(parsed_person)   # Check if parsed data is in the DB
        self.person_tg_id = shift_item[0]
        self.today_date = dt.datetime.today()
        self.shifts_date = dt.date.today() + dt.timedelta(days=1)
        self.creator_tg_id = creator_tg_id
        notify(self.person_tg_id, self.post_name)
        self.notified.append(shift_item)            # Add and monitor notification status

    def set_post(self, post_id: int) -> None:
        """Set post for current employee"""

        self.post_id = post_id


def validate_data(parsed_person: [str]) -> [str]:
    """Validate incoming person credentials with DB"""
    cursor = db.get_cursor()
    cursor.execute(f"SELECT id, last_name, first_name, mid_name FROM person WHERE last_name='{parsed_person[0]}' ")
    db_results = cursor.fetchall()
    if db_results is None or not db_results:
        raise exceptions.NotCorrectMessage(settings.message['name_err'])
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
        raise exceptions.NotCorrectMessage(settings.message['surname_err'])


def notify(person_tg_id: int, post_name: str):
    """Create answer message for telegram dispatcher"""
    sender.send_message(tg_id=str(person_tg_id),
                        text=f'Ты заступаешь завтра: {post_name}',
                        keyboard=markup.agree_inline_menu)


def parse_message(text: str) -> [str]:
    """Parse message text to find surnames"""
    text: str = to_ru_letters(text.lower())
    parsed_text: Optional[Match[str]] = re.search(r'(\b[а-яё]{2,20}\b ?[а-я]?\.? ?[а-я]?\.?)', text)
    if parsed_text is None or not parsed_text.group(0):
        raise exceptions.NotCorrectMessage(settings.message['name_err'])
    person_name: str = parsed_text.group(0).replace('ё', 'е')
    return person_name.replace('.', ' ').split()


def to_ru_letters(word: str) -> str:
    """Fix similar_letters was taking by mistake in another language"""
    similar_letters: dict[str, str] = {'en': 'abceghkmnoprtuxy',
                                       'ru': 'авседнкмпоргтиху'}
    result: str = ''
    for letter in word:
        if letter in similar_letters['en']:
            index: int = similar_letters['en'].index(letter)
            result += similar_letters['ru'][index]
        else:
            result += letter
    return result


new_shift: Shift = Shift()

if __name__ == '__main__':
    new_shift.add_shift('Смaгин Д.A.', '220697264')
