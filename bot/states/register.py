from aiogram.dispatcher.filters.state import State, StatesGroup


class RegisterState(StatesGroup):
    """
    Класс конечного автомата
    """
    waiting_for_send_fio = State()
    waiting_for_send_address = State()
    waiting_for_send_city = State()
