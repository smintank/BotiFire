import os
from typing import Any, Optional
import sqlite3

from config_data.config import DB_NAME, DB_PATH, REWRITE_DB


def insert(table: str,
           column_values: dict
           ):
    values = [tuple(column_values.values())]
    columns = ', '.join(column_values.keys())
    placeholders = ", ".join("?" * len(column_values.keys()))
    cursor.executemany(
        f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        , values)
    conn.commit()


def update(table: str,
           column_values: dict,
           condition: str
           ):
    values = [tuple(column_values.values())]
    query = " = ?, ".join(column_values.keys())
    query += ' = ? '
    cursor.executemany(
        f"UPDATE {table} SET {query} WHERE {condition}",
        values)
    conn.commit()


def fetchall(table: str,
             columns: list[str],
             filters: Optional[str] = None,
             order_by: Optional[str] = None
             ) -> list[dict[str, Any]]:
    """Return columns from the table"""
    columns_joined = ", ".join(columns)
    query = f"SELECT {columns_joined} FROM {table} "
    if filters:
        query += f'WHERE {filters} '
    if order_by:
        query += f'ORDER BY {order_by};'
    cursor.execute(query)
    rows = cursor.fetchall()
    result = []
    for row in rows:
        dict_row = {}
        for index, column in enumerate(columns):
            dict_row[column] = row[index]
        result.append(dict_row)
    return result


def delete(table: str, row_id: int) -> None:
    """Delete row from table of DB"""
    row_id: int = int(row_id)
    cursor.execute(f"DELETE FROM {table} WHERE id={row_id}")
    conn.commit()


def get_cursor():
    """Return DB cursor"""
    return cursor


def _init_db() -> None:
    """Initialize DB"""
    with open('database/create_db.sql', 'r') as f:
        sql: str = f.read()
    cursor.executescript(sql)
    conn.commit()
    fill_table()


def check_db_exists() -> None:
    """Create DB if DB is not exist"""
    cursor.execute("SELECT name FROM sqlite_master "
                   "WHERE type='table' AND name='employee'")
    table_exists = cursor.fetchall()
    if table_exists:
        return
    _init_db()


def fill_table() -> None:
    """Fill DB with start data"""
    with open('database/fill_db.sql', 'r') as f:
        sql: str = f.read()
    cursor.executescript(sql)
    conn.commit()


def _del_db():
    """Delete current DB"""
    try:
        os.remove(os.path.join(f'{DB_PATH}', f'{DB_NAME}'))
    except FileExistsError:
        pass


if REWRITE_DB:
    _del_db()


conn = sqlite3.connect(os.path.join(f'{DB_PATH}', f'{DB_NAME}'))
cursor = conn.cursor()
check_db_exists()
