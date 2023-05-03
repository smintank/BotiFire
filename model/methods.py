from dataclasses import dataclass
from typing import Optional
import datetime as dt

from bot import bot
from database import database as db
from keyboards.menu_keyboards import get_service_keyboard
from lexicon import menu_buttons


@dataclass
class Post:
    name: str
    alias: str
    is_busy: Optional[bool] = False


@dataclass
class Employee:
    tg_id: str
    name: str
    is_busy: Optional[bool] = False
    status: str = '🟨'


@dataclass()
class Shift:
    post: Post
    employee: Optional[Employee] = None
    is_notify: Optional[bool] = False


shifts: dict[str: Shift] = {}
posts: dict[str: Post] = {}
employees: dict[str: Employee] = {}
current_post: Optional[Post] = None


def get_shift() -> dict[str: str]:
    """Get current shift buttons"""
    buttons: dict[str: str] = {}
    for name, shift in shifts.items():
        if shift.employee is None:
            buttons[name] = shift.post.alias
        else:
            text = f'{shift.post.alias} - {shift.employee.name} {shift.employee.status}'
            buttons[name] = text
    return buttons


def get_employees() -> dict[str: str]:
    buttons: dict[str: str] = {}
    for tg_id, employee in employees.items():
        if not employee.is_busy:
            buttons[tg_id] = employee.name
    return buttons


def set_shift(shift: dict[str: str], creator: str, offset: int = 1) -> None:
    post = shift['post']
    employee = shift['employee']
    post_id = db.fetchall('post', ['id'], f'name == "{post}"')
    post_id = str(post_id[0]['id'])
    values: dict = {
        'employee_id': employee[3:],
        'post_id': post_id,
        'creator_id': creator,
        'workday_date': _get_date(offset)
    }
    if shifts[post].employee is None:
        db.insert('day_post_employee', values)
    else:
        condition = f'post_id = "{post_id}"'
        db.update('day_post_employee', values, condition=condition)
    _set_local_shifts(post, employee)


async def send_messages():
    notified_shifts: dict[str: str] = _get_post_employee()
    for employee, post in notified_shifts.items():
        text: str = menu_buttons.NOTIFY_MESSAGE.format(post=shifts[post].post.alias.lower())
        markup = get_service_keyboard(['ok'])
        await bot.send_message(chat_id=employee, text=text, reply_markup=markup)


def _get_post_employee() -> dict[str: str]:
    result: dict[str: str] = {}
    for shift in shifts.values():
        if shift.employee is not None:
            result[shift.employee.tg_id] = shift.post.name
    return result


def _set_local_shifts(post: str, employee: str) -> None:
    if shifts[post].employee is not None:
        changed_employee: Employee = shifts[post].employee
        changed_employee.is_busy = False
    shifts[post].employee = employees[employee]
    employees[employee].is_busy = True


def _get_date(offset: int) -> str:
    if 0 <= dt.datetime.utcnow().hour <= 7:
        offset -= 1
    date = dt.date.today() + dt.timedelta(days=offset)
    return date.strftime('%Y-%m-%d')


def _fetchall_employees() -> None:
    """Fetch employees from db and add it to shift class in {id_2345523: 'Name F.M.}' format"""
    results = db.fetchall(table='employee',
                         columns=['last_name', 'first_name', 'mid_name', 'id'],
                         order_by='last_name')
    for result in results:
        name = f'{result["last_name"]} {result["first_name"][0]}.{result["mid_name"][0]}.'.title()
        tg_id = result["id"]
        employees[f'id_{result["id"]}'] = Employee(tg_id, name)


def _fetchall_posts(is_main_posts: bool = True) -> None:
    """Clear posts values"""
    results = db.fetchall(table='post',
                         columns=['name', 'alias'],
                         filters=f'is_main={str(is_main_posts)}',
                         order_by='ordering')
    for result in results:
        posts[result['name']] = Post(result['name'], result['alias'], )


def _fill_shifts() -> None:
    for name, post in posts.items():
        shifts[name] = Shift(post=post)


_fetchall_employees()
_fetchall_posts()
_fill_shifts()
