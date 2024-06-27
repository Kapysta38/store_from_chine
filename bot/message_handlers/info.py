from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from .base import BaseHandler
from ..dependence import error
from ..api import APIClient


class InfoHandler(BaseHandler):
    command = ['info']
    callback_data = 'info'
    title = 'Вызов меню'

    @error(title=title)
    async def start_handler(self, message: Message, state: FSMContext):
        """
        Этот обработчик будет вызван, когда пользователь отправит команду `/info`.
        """
        chat_id = message.chat.id
        if chat_id >= 0:
            client = APIClient()
            current_user = await client.get_filter_users(tg_id=chat_id)
            if not current_user:
                return await self.handle(message.chat.id, state=False)
            current_user = current_user[0]
            return await self.handle(message.chat.id, edit_text=[current_user["full_name"], current_user["address"]])

    @staticmethod
    async def run_handler(message, state):
        await InfoHandler().start_handler(message, state)
