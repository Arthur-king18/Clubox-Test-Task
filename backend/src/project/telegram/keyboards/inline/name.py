from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def get_choose_name(name: str) -> InlineKeyboardMarkup:
    kb = [
        [
            InlineKeyboardButton(text=f"Call me {name}", callback_data='my_name'),
        ],
        [
            InlineKeyboardButton(text="That's not my real name", callback_data='other_name')
        ]
    ]

    choose_name_inline_kb = InlineKeyboardMarkup(row_width=1, inline_keyboard=kb)

    return choose_name_inline_kb
