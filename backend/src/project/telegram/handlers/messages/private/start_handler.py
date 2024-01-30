from aiogram.filters import CommandStart
from aiogram.types import Message

from backend.src.project.db.models import User
from backend.src.project.telegram import dp
from backend.src.project.telegram.keyboards.inline import get_choose_name
from backend.src.project.telegram.utils.answer import answer
from backend.src.project.telegram.utils.handler import handler
from backend.src.project.telegram.keyboards.inline import get_profile


@dp.message(CommandStart())
@handler
async def command_start(message: Message) -> None:
    user = await User.get_or_none(id=message.chat.id)

    is_registered = bool(user.age)

    if not is_registered:
        await answer(
            message=message,
            chat_id=message.chat.id,
            text="Hi there! What's your real name?!",
            reply_markup=await get_choose_name(name=message.from_user.first_name)
        )

    else:
        await answer(
            message=message,
            chat_id=message.chat.id,
            text="You are already registered!",
            reply_markup=await get_profile()
        )
