from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from .base import BaseHandler
from ..dependence import error
from ..api import APIClient
from ..utils import get_users_in_chat_role


class OrderHandler(BaseHandler):
    callback_data = 'order'
    title = 'Новый заказ'
    text_startswith = "https://"

    @error(title=title)
    async def start_handler(self, message: Message, state: FSMContext):
        """
        Этот обработчик будет вызван, когда пользователь отправит команду `/info`.
        """
        chat_id = message.chat.id
        client = APIClient()
        current_user = await client.get_filter_users(tg_id=chat_id)
        if chat_id >= 0 and current_user:
            admin_chat = await get_users_in_chat_role(client)
            if admin_chat:
                admin_chat = admin_chat[0]

            current_user = current_user[0]

            url = message.text
            await self.bot.delete_message(message.chat.id, message.message_id)

            order = await client.create_order(current_user['user_id'], url)

            await self.handle(chat_id, state="user",
                              edit_text=[order['order_id'], current_user['full_name'], current_user['address'], url])

            await self.handle(admin_chat,
                              edit_text=[order['order_id'], current_user['full_name'], current_user['address'], url])

    @staticmethod
    async def run_handler(message, state):
        await OrderHandler().start_handler(message, state)
