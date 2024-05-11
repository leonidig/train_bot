from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

go_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="До головного меню", callback_data="go_home")
    ]
])



