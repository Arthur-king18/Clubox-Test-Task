from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def change_name_and_age() -> InlineKeyboardMarkup:
    kb = [
        [
            InlineKeyboardButton(text=f"Change name", callback_data='change_name'),
        ],
        [
            InlineKeyboardButton(text="Change age", callback_data='change_age')
        ],
        [
            InlineKeyboardButton(text=f"⬅ Back", callback_data='back_menu'),
        ]
    ]

    change_name_and_age_inline_kb = InlineKeyboardMarkup(row_width=1, inline_keyboard=kb)

    return change_name_and_age_inline_kb
