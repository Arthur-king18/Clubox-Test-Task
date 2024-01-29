from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from backend.src.project.telegram import dp
from backend.src.project.telegram.utils.answer import answer
from backend.src.project.telegram.utils.handler import handler

from backend.src.project.telegram.states import Form

from backend.src.project.telegram.filters import is_valid_age


@dp.message_handler(state=Form.age)
@handler
async def command_get_age(message: Message, state: FSMContext) -> None:
    if is_valid_age(age=message.text):
        await state.update_data(age=message.text)

        await state.set_state(Form.age)

        await answer(
            message=message,
            chat_id=message.chat.id,
            text="Well"  # Меню с веб апп и дать право исправлять
        )

        # Регистрация пользователя

    else:
        return
