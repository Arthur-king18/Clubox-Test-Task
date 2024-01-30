from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from backend.src.project.telegram import dp
from backend.src.project.telegram.states import Form
from backend.src.project.telegram.utils.answer import answer
from backend.src.project.telegram.utils.handler import handler
from backend.src.project.db.models import User


@dp.callback_query(lambda callback_query: callback_query.data == "my_name")
@handler
async def command_get_my_name(query: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(Form.name)

    await User.update_call_name(call_name=query.message.chat.first_name)

    await state.set_state(Form.age)

    await answer(
        message=query.message,
        chat_id=query.message.chat.id,
        text="Good! How old are you?"
    )

@dp.callback_query(lambda callback_query: callback_query.data == "other_name")
@handler
async def command_get_other_name(query: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(Form.name)

    await answer(
        message=query.message,
        chat_id=query.message.chat.id,
        text="⬇ Write your name ⬇"
    )

