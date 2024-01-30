from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from backend.src.project.telegram import dp
from backend.src.project.telegram.utils.answer import answer
from backend.src.project.telegram.utils.handler import handler
from backend.src.project.telegram.states import Form
from backend.src.project.db.models import User
from backend.src.project.telegram.keyboards.inline import back_menu

@dp.message(StateFilter(Form.name))
@handler
async def command_write_other_name(message: Message, state: FSMContext) -> None:
    user = await User.get_or_none(id=message.chat.id)

    if not bool(user.call_name):
        await User.update_call_name(call_name=message.text)

        await state.set_state(Form.age)

        await answer(
            message=message,
            chat_id=message.chat.id,
            text="Good! How old are you?"
        )

    else:
        await User.update_call_name(call_name=message.text)

        await answer(
            message=message,
            chat_id=message.chat.id,
            text=f"Well! Your current name is <b>{message.text}</b>",
            reply_markup=await back_menu()
        )

        await state.clear()