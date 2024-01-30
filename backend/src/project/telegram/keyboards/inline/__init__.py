from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from backend.src.project.telegram.keyboards.inline.name import get_choose_name
from backend.src.project.telegram.keyboards.inline.profile import get_profile
from backend.src.project.telegram.keyboards.inline.change_name_and_age import change_name_and_age
from backend.src.project.telegram.keyboards.inline.back import back_menu


def create_keyboard(*buttons: types.InlineKeyboardButton) -> types.InlineKeyboardMarkup:
    return InlineKeyboardBuilder().add(*buttons).adjust(1).as_markup()
