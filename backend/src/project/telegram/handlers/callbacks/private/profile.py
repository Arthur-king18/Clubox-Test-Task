from aiogram.types import CallbackQuery

from backend.src.project.telegram import dp
from backend.src.project.telegram.utils.answer import answer
from backend.src.project.telegram.utils.handler import handler
from backend.src.project.telegram.keyboards.inline import change_name_and_age
from backend.src.project.db.models import User


@dp.callback_query(lambda callback_query: callback_query.data == "profile")
@handler
async def command_profile(query: CallbackQuery) -> None:
    user = await User.get_or_none(id=query.message.chat.id)

    await answer(
        message=query.message,
        chat_id=query.message.chat.id,
        text=f"ID - <b>{user.id}</b>\n"
             f"Name - <b>{user.call_name}</b>\n"
             f"Age - <b>{user.age}</b>\n\n"
             "What do you want to change? 👀",
        reply_markup=await change_name_and_age()
    )
