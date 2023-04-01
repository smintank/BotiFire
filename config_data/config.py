from typing import NamedTuple


class DataBase(NamedTuple):
    NAME: str = 'shifts.db'
    PATH: str = 'database/db'
    REWRITE_DB: bool = True
