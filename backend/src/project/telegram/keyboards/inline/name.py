from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def get_choose_name(name: str) -> InlineKeyboardMarkup:
    choose_choose_name_inline_kb = InlineKeyboardMarkup(row_width=1)

    my_name = InlineKeyboardButton(text=f"Call me {name}", callback_data='my_name')
    other = InlineKeyboardButton(text="That's not my real name", callback_data='other_name')

    choose_choose_name_inline_kb.add(my_name).add(other)

    return choose_choose_name_inline_kb
