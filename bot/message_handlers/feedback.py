from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from .base import BaseHandler
from ..api import APIClient
from ..dependence import error
from ..states import FeedbackState
from ..utils import get_users_in_chat_role


class FeedbackHandler(BaseHandler):
    command = ["feedback"]
    callback_data = 'feedback'
    state = FeedbackState
    title = 'Обратная связь'

    @error(title=title)
    async def waiting_for_send_feedback(self, message: Message, state: FSMContext):
        chat_id = message.from_user.id

        user_data = await state.get_data()
        await state.finish()
        message_id = user_data['message_id']

        text = message.text[:255]
        await self.bot.delete_message(message.chat.id, message.message_id)

        client = APIClient()
        current_user = await client.get_filter_users(tg_id=chat_id)
        if not current_user:
            return await self.handle(chat_id, message_id, False)
        current_user = current_user[0]
        feedback = await client.create_feedback(current_user['user_id'], text=text)
        admin_chat = await get_users_in_chat_role(client)

        await self.handle(chat_id, message_id, edit_text=[feedback['id']], state=True)
        await self.handle(admin_chat[0], state="admin",
                          edit_text=[feedback['id'], current_user['full_name'], current_user['username'], text],
                          edit_callback=[feedback['id']])

    @staticmethod
    async def reg_waiting_for_send_feedback(message: Message, state: FSMContext):
        return await FeedbackHandler().waiting_for_send_feedback(message, state)

    @error(title=title)
    async def start_handler(self, message: Message, state: FSMContext):
        """
        Этот обработчик будет вызван, когда пользователь отправит команду `/feedback`.
        :param message: types.Message
        """
        chat_id = message.chat.id
        if chat_id >= 0:
            await state.finish()
            await self.state.waiting_for_send_feedback.set()

            msg = await self.handle(chat_id)
            await state.update_data(message_id=msg['message_id'])

    @staticmethod
    async def run_handler(message, state):
        await FeedbackHandler().start_handler(message, state)
