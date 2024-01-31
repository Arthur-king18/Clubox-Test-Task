from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

from backend.src.project.settings import settings


async def get_profile(user_id: str) -> InlineKeyboardMarkup:
    kb = [
        [
            InlineKeyboardButton(text="My profile 📺", callback_data='profile'),
        ],
        [
            InlineKeyboardButton(text="Tap-tap",
                                 web_app=WebAppInfo(url=f"https://{settings.DOMAIN}/api/telegram/user/{user_id}")),
        ]
    ]

    profile_inline_kb = InlineKeyboardMarkup(row_width=1, inline_keyboard=kb)

    return profile_inline_kb
