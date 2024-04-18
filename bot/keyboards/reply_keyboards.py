from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData


main_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text = 'Test - 1')
    ],
    [
        KeyboardButton(text = 'Test - 2')
    ],
    [
        KeyboardButton(text = 'Test - 3')
    ]
])