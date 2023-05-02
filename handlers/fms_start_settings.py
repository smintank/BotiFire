from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.state import State


class FSMUserSettings(MemoryStorage):
    fill_nik = State()
    fill_subscriptions = State()