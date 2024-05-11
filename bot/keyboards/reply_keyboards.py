from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


subjects_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Алгебра")
    ], 
    [
        KeyboardButton(text="Географія")
    ],
    [
        KeyboardButton(text="Перекладач")
    ]
])


#        A  L  G  E  B  R  A

algebra1 = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="72")
    ],
    [
        KeyboardButton(text="12")
    ],
    [
        KeyboardButton(text="288")
    ],
    [
        KeyboardButton(text="10")
    ]
])


algebra2 = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="21")
    ],
    [
        KeyboardButton(text="-3")
    ],
    [
        KeyboardButton(text="25")
    ]
])


algebra3 = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="8")
    ],
    [
        KeyboardButton(text="64")
    ],
    [
        KeyboardButton(text="32")
    ]
])


algebra4 = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="27")
    ],
    [
        KeyboardButton(text="73")
    ],
    [
        KeyboardButton(text="Інше")
    ]
])



continue_kb1 = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Продовжити")
    ]
])

continue_kb2 = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Далі")
    ]
])

continue_kb3 = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Поїхали")
    ]
])


continue_kb4 = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Закінчити опитування")
    ]
])


cont_g1 = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="До наступного питання")
    ]
])


cont_g2 = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="->")
    ]
])


cont_g3 = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Далі!!!")
    ]
])


cont_g4 = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Завершити тест")
    ]
])


translator_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="❌")
    ],
    [
        KeyboardButton(text="🔄️")
    ]
],resize_keyboard=True)