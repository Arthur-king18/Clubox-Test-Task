from aiogram import types
from backend.src.project.telegram.events.delete import DeleteEvent

from backend.src.project.telegram import dp
from backend.src.project.telegram.utils.handler import handler


@dp.callback_query(DeleteEvent.filter())
@handler
async def delete(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.answer()
