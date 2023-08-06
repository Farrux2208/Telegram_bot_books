
from aiogram.dispatcher.filters.state import StatesGroup, State

class InfoState(StatesGroup):
    text = State()