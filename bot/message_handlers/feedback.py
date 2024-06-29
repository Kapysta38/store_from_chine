from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

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


class FeedbackAnswerHandler(FeedbackHandler):
    command = None
    callback_data = 'send_answer'
    title = 'Ответ обратной связи'

    @error(title=title)
    async def run(self, callback: CallbackQuery, state: FSMContext, data: str = None):
        chat_id, message_id = callback.message.chat.id, callback.message.message_id
        template, status = await self.get_template_and_status(callback, state, data=data)
        await self.handle(chat_id, message_id, edit_text=template, state=status)
        await self.set_state(state, chat_id, message_id, data=data)

    @staticmethod
    async def reg_waiting_for_send_answer(message: Message, state: FSMContext):
        return await FeedbackAnswerHandler().waiting_for_send_answer(message, state)

    @error(title=title)
    async def waiting_for_send_answer(self, message: Message, state: FSMContext):
        chat = message.from_user.id

        user_data = await state.get_data()
        await state.finish()
        message_id = user_data['message_id']
        feedback_id = user_data['feedback_id']
        from_user_tg_id = user_data['from_user_tg_id']

        if from_user_tg_id != chat:
            await self.set_state(state, message_id=message_id, data=feedback_id)
            await state.update_data(from_user_tg_id=from_user_tg_id)
            return

        text = message.text[:255]
        await self.bot.delete_message(message.chat.id, message.message_id)

        client = APIClient()
        feedback = await client.update_feedback(feedback_id, answer=text)
        user = await client.get_user(feedback['user_id'])

        await self.handle(message.chat.id, message_id, state=True,
                          edit_text=[feedback['id'], user['full_name'], user['username'], feedback['text'],
                                     feedback['answer']])

        await self.handle(user['tg_id'], state='user', edit_text=[feedback['id'], feedback['text'], feedback['answer']])

    async def get_template_and_status(self, callback: CallbackQuery, state: FSMContext, data: str = None):
        if data:
            await state.finish()
            await state.update_data(from_user_tg_id=callback.from_user.id)

            client = APIClient()
            feedback = await client.get_feedback(int(data))
            user = await client.get_user(feedback['user_id'])

            template = [feedback['id'], user['full_name'], user['username'], feedback['text']]
            return template, None
        return None, None

    async def set_state(self, state: FSMContext, chat_id: int = None, message_id: int = None, data=None):
        if data:
            user_data = await state.get_data()
            await self.state.waiting_for_send_answer.set()
            await state.update_data(message_id=message_id, feedback_id=data, from_user_tg_id=user_data['from_user_tg_id'])
