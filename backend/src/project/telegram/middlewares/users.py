from typing import Callable

from aiogram import BaseMiddleware
from aiogram import types, Bot

from backend.src.project.db.models import User


class UserMiddleware(BaseMiddleware):
    async def __call__(self, handler: Callable, event: types.TelegramObject, data: dict):
        user = await User.get_current()
        bot = Bot.get_current()

        data['user'] = user
        message = dict(event)["message"]

        try:
            await bot.delete_message(chat_id=dict(event)["message"].chat.id, message_id=message.message_id - 1)
        except:
            pass

        return await handler(event, data)
