from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart

from backend.src.project.telegram import dp
from backend.src.project.telegram.utils.answer import answer
from backend.src.project.telegram.utils.handler import handler

from backend.src.project.telegram.states import Form

from backend.src.project.telegram.keyboards.inline import get_choose_name


@dp.message(CommandStart())
@handler
async def command_start(message: Message, state: FSMContext) -> None:

    await answer(
        message=message,
        chat_id=message.chat.id,
        text="Hi there! What's your real name?!",
        reply_markup=await get_choose_name(name=message.from_user.first_name)
    )
