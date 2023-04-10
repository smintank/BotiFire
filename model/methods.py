from sqlite3 import Cursor
from aiogram.types import InlineKeyboardMarkup
from typing import NamedTuple
from database import database as db
from keyboards.menu_keyboards import get_keyboard


class Shift:
    posts: dict[str: dict[str: str]] = {}
    current_post: str = ''
    employees: dict[str: str] = {}


def get_shift() -> InlineKeyboardMarkup:
    return get_keyboard(_merge_text(shift.posts))


def posts_employee_process(post_name: str) -> InlineKeyboardMarkup:
    shift.current_post = post_name
    if not shift.employees:
        _fetch_employees()
    return get_keyboard(shift.employees, width=3, last_btn='cancel')


def _employee_process(employee: str) -> None:
    if shift.current_post != '':
        _set_employee_on_post(shift.current_post, employee)


def _merge_text(dictionary: dict[str: dict[str: str]]) -> dict[str: str]:
    dict_copy: dict[str: str] = {}
    for key, value in dictionary.items():
        if value['employee']:
            dict_copy[key] = '✅' + value['post'] + '-' + value['employee']
        else:
            dict_copy[key] = value['post']
    return dict_copy


def _set_employee_on_post(post: str, employee: str) -> None:
    shift.posts[post]['employee'] = employee


def _fetch_employees() -> None:
    result = _fetch_employees_from_db()
    for employee in result:
        full_name: str = f'{employee[0].capitalize()} {employee[1][0].upper()}.{employee[2][0].upper()}.'
        shift.employees[f'id_{employee[3]}'] = full_name


def _fetch_employees_from_db() -> list[tuple]:
    cursor: Cursor = db.get_cursor()
    cursor.execute(f"SELECT last_name, first_name, mid_name, id FROM person")
    return cursor.fetchall()


def _clear_posts(is_main_posts: bool = True) -> None:
    """Clear posts values"""
    cursor: Cursor = db.get_cursor()
    cursor.execute(f"SELECT name, alias FROM post WHERE is_main={str(is_main_posts)}")
    result = cursor.fetchall()
    for post in result:
        shift.posts[post[0]] = {'post': post[1], 'employee': ''}


shift = Shift()
_clear_posts()