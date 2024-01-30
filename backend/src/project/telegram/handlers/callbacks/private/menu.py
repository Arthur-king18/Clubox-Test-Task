from aiogram.types import CallbackQuery

from backend.src.project.db.models import User
from backend.src.project.telegram import dp
from backend.src.project.telegram.utils.answer import answer
from backend.src.project.telegram.utils.handler import handler
from backend.src.project.telegram.keyboards.inline import get_profile


@dp.callback_query(lambda callback_query: callback_query.data == "back_menu")
@handler
async def command_menu(query: CallbackQuery) -> None:
    user = await User.get_or_none(id=query.message.chat.id)

    is_registered = bool(user.age)

    if not is_registered:

        await answer(
            message=query.message,
            chat_id=query.message.chat.id,
            text="Click on /start and register"
        )

    else:
        await answer(
            message=query.message,
            chat_id=query.message.chat.id,
            text="<b>I'm glad to see you</b> 🎈",
            reply_markup=await get_profile()
        )
