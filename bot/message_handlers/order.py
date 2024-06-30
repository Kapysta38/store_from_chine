import traceback

from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from .base import BaseHandler
from ..dependence import error
from ..api import APIClient
from ..utils import get_users_in_chat_role
from ..config.logging_config import logger as log


class OrderHandler(BaseHandler):
    callback_data = 'order'
    title = 'Создание нового заказа'
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
                              edit_text=[order['order_id'], current_user['full_name'], "",
                                         f"г. {current_user['city']}, {current_user['address']}",
                                         url])

            await client.update_user(current_user['user_id'], username=message.chat.username)

            await self.handle(admin_chat,
                              edit_text=[order['order_id'], current_user['full_name'], f"(@{message.chat.username})",
                                         f"г. {current_user['city']}, {current_user['address']}", url],
                              edit_callback=[order['order_id'], order['order_id']])

    @staticmethod
    async def run_handler(message, state):
        await OrderHandler().start_handler(message, state)


class AcceptOrderHandler(BaseHandler):
    callback_data = 'accept_order'
    title = 'Подтверждение заказа'
    new_state = 1  # success

    @error(title=title)
    async def run(self, callback: CallbackQuery, state: FSMContext, data: str = None):
        chat_id, message_id = callback.message.chat.id, callback.message.message_id
        template, status = await self.get_template_and_status(callback, state, data=data)
        await self.handle(chat_id, message_id, edit_text=template, state=status)
        await self.set_state(state, chat_id, message_id, data=data)

    async def get_template_and_status(self, callback: CallbackQuery, state: FSMContext, data: str = None):
        if data:
            try:
                client = APIClient()
                order = await client.update_order(int(data), order_status=self.new_state)
                user = await client.get_user(order['user_id'])
                template = [order['order_id'], user['full_name'], "", f"г. {user['city']}, {user['address']}",
                            order['product_url']]
                await self.handle(user["tg_id"], edit_text=template)
                template[2] = f"(@{user['username']})"
                return template, None
            except Exception as ex:
                log.error({"error": ex, "traceback": traceback.format_exc()})
                return None, False
        return None, False


class DeclineOrderHandler(AcceptOrderHandler):
    callback_data = 'decline_order'
    title = 'Отклонение заказа'
    new_state = 2  # failed
