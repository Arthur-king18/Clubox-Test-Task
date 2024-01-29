from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from backend.src.project.telegram import dp
from backend.src.project.telegram.utils.answer import answer
from backend.src.project.telegram.utils.handler import handler

from backend.src.project.telegram.states import Form


@dp.message_handler(state=Form.name)
@handler
async def command_write_other_name(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)

    await state.set_state(Form.age)

    await answer(
        message=message,
        chat_id=message.chat.id,
        text="Good! How old are you?"
    )