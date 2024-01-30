from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def back_menu() -> InlineKeyboardMarkup:
    kb = [
        [
            InlineKeyboardButton(text=f"⬅ Back", callback_data='back_menu'),
        ],
    ]

    back_menu_inline_kb = InlineKeyboardMarkup(row_width=1, inline_keyboard=kb)

    return back_menu_inline_kb
