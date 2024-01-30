from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def get_profile() -> InlineKeyboardMarkup:
    kb = [
        [
            InlineKeyboardButton(text="My profile 📺", callback_data='profile'),
        ]
    ]

    profile_inline_kb = InlineKeyboardMarkup(row_width=1, inline_keyboard=kb)

    return profile_inline_kb
