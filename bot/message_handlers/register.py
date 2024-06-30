import datetime

from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from .base import BaseHandler
from ..api import APIClient
from ..dependence import error
from ..states import RegisterState


class RegisterHandler(BaseHandler):
    callback_data = "register"
    state = RegisterState
    title = 'Регистрация'

    @error(title=title + " [ввод ФИО]")
    async def waiting_for_send_fio(self, message: Message, state: FSMContext):
        chat_id = message.from_user.id

        user_data = await state.get_data()
        await state.finish()
        message_id = user_data['message_id']

        text = message.text[:255]
        await self.bot.delete_message(message.chat.id, message.message_id)

        await state.update_data(full_name=text)

        await self.set_state(state, chat_id, message_id)

        await self.handle(chat_id, message_id, "enter_city")

    @error(title=title + " [ввод города]")
    async def waiting_for_send_city(self, message: Message, state: FSMContext):
        chat_id = message.from_user.id

        user_data = await state.get_data()
        await state.finish()
        message_id = user_data['message_id']
        if 'full_name' not in user_data:
            await self.set_state(state, chat_id, message_id)
            return await self.handle(chat_id, message_id, None)
        full_name = user_data['full_name']

        city = message.text[:255]
        await self.bot.delete_message(message.chat.id, message.message_id)

        await state.update_data(full_name=full_name, city=city)

        await self.set_state(state, chat_id, message_id)

        await self.handle(chat_id, message_id, "enter_address")

    @error(title=title + " [ввод адреса]")
    async def waiting_for_send_address(self, message: Message, state: FSMContext):
        chat_id = message.from_user.id

        user_data = await state.get_data()
        await state.finish()
        message_id = user_data['message_id']
        if 'full_name' not in user_data or 'city' not in user_data:
            await self.set_state(state, chat_id, message_id)
            return await self.handle(chat_id, message_id, None)
        full_name = user_data['full_name']
        city = user_data['city']

        address = message.text[:255]
        await self.bot.delete_message(message.chat.id, message.message_id)

        client = APIClient()
        exist_user = await client.get_filter_users(tg_id=chat_id)
        if not exist_user:
            await client.create_user(tg_id=chat_id, full_name=full_name, address=address,
                                     username=message.chat.username, city=city)
        else:
            await client.update_user(exist_user[0]['user_id'], full_name=full_name, address=address,
                                     username=message.chat.username, city=city)

        await self.handle(chat_id, message_id, "success")

    @staticmethod
    async def reg_waiting_for_send_fio(message: Message, state: FSMContext):
        return await RegisterHandler().waiting_for_send_fio(message, state)

    @staticmethod
    async def reg_waiting_for_send_address(message: Message, state: FSMContext):
        return await RegisterHandler().waiting_for_send_address(message, state)

    @staticmethod
    async def reg_waiting_for_send_city(message: Message, state: FSMContext):
        return await RegisterHandler().waiting_for_send_city(message, state)

    async def set_state(self, state: FSMContext, chat_id: int = None, message_id: int = None, data=None):
        user_data = await state.get_data()
        if 'full_name' not in user_data and 'city' not in user_data:
            await state.finish()
            await self.state.waiting_for_send_fio.set()
        elif 'city' in user_data and 'full_name' in user_data:
            await self.state.waiting_for_send_address.set()
        else:
            await self.state.waiting_for_send_city.set()
        await state.update_data(message_id=message_id)
