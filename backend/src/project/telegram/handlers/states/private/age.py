from aiogram.filters import StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from backend.src.project.telegram import dp
from backend.src.project.telegram.utils.answer import answer
from backend.src.project.telegram.utils.handler import handler

from backend.src.project.telegram.states import Form

from backend.src.project.db.models import User
from backend.src.project.telegram.filters import is_valid_age
from backend.src.project.telegram.keyboards.inline import get_profile


@dp.message(StateFilter(Form.age))
@handler
async def command_get_age(message: Message, state: FSMContext) -> None:
    user = await User.get_or_none(id=message.chat.id)

    if await is_valid_age(age=message.text):
        if not bool(user.age):
            await answer(
                message=message,
                chat_id=message.chat.id,
                text="<b>Congratulations!</b> 🥳",
                reply_markup=await get_profile()
            )

            await User.update_age(age=message.text)

            await state.clear()

        else:
            await answer(
                message=message,
                chat_id=message.chat.id,
                text=f"Well! Your current age is <b>{message.text}</b>",
                reply_markup=await get_profile()
            )

            await User.update_age(age=message.text)

            await state.clear()

    else:
        await answer(
            message=message,
            chat_id=message.chat.id,
            text="Incorrect age. Try again"
        )

