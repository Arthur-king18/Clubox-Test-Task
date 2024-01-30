from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import get_i18n

from backend.src.project.db.models import User
from backend.src.project.settings import settings
from backend.src.project.telegram import dp
from backend.src.project.telegram.handlers.messages.private.start_handler import command_start
from backend.src.project.telegram.utils.handler import handler


@dp.message(Command('restart'), lambda _: settings.DEBUG)
@handler
async def restart(message: types.Message, user: User, state: FSMContext):
    await user.delete()
    await command_start(message, state=state)


@dp.message(Command('locales'), lambda _: settings.DEBUG)
@handler
async def locales(_: types.Message):
    i18n = get_i18n()
    i18n.reload()
