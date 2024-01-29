from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from backend.src.project.telegram.keyboards.inline.name import get_choose_name


def create_keyboard(*buttons: types.InlineKeyboardButton) -> types.InlineKeyboardMarkup:
    return InlineKeyboardBuilder().add(*buttons).adjust(1).as_markup()
