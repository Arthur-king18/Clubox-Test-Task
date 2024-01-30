from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from backend.src.project.telegram import dp
from backend.src.project.telegram.states import Form
from backend.src.project.telegram.utils.answer import answer
from backend.src.project.telegram.utils.handler import handler


@dp.callback_query(lambda callback_query: callback_query.data == "change_name")
@handler
async def command_change_name(query: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(Form.name)

    await answer(
        message=query.message,
        chat_id=query.message.chat.id,
        text="⬇ Write <b>new name</b> bellow ⬇",
    )

@dp.callback_query(lambda callback_query: callback_query.data == "change_age")
@handler
async def command_change_age(query: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(Form.age)

    await answer(
        message=query.message,
        chat_id=query.message.chat.id,
        text="⬇ Write your <b>age</b> bellow ⬇",
    )