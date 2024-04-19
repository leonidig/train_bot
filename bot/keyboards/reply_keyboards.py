from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData


main_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text = 'Basketball')
    ],
    [
        KeyboardButton(text = 'Dice')
    ],
    [
        KeyboardButton(text = 'Casino')
    ],
    [
        KeyboardButton(text = 'Football')
    ]
])