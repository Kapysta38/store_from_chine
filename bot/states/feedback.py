from aiogram.dispatcher.filters.state import State, StatesGroup


class FeedbackState(StatesGroup):
    """
    Класс конечного автомата
    """
    waiting_for_send_feedback = State()
    waiting_for_send_answer = State()
