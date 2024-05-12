import asyncio
import logging
import sys
from os import getenv, listdir, path
import types
from dotenv import load_dotenv


from aiogram import Bot, Dispatcher, html, Router, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.filters.callback_data import CallbackData,  CallbackQuery
from aiogram.utils.markdown import hbold
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReactionTypeEmoji, FSInputFile, InputMediaPhoto, InputMediaVideo


from keyboards import reply_keyboards, inline_keyboards
from commands import commands_router
from utils.states import Algebra, Geography, Translate


from translators import translate_text



load_dotenv()
print(getenv("TOKEN"))
TOKEN = getenv("TOKEN")




router = Router()
dp = Dispatcher()
dp.include_router(commands_router)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привіт, {hbold(message.from_user.full_name)}!", reply_markup=reply_keyboards.subjects_kb)



@dp.message(F.text == "Алгебра")
async def st_alg_quiz(message: Message, state: FSMContext):
    await state.set_state(Algebra.q1)
    await message.reply("Це режим відповіді на запитання з Алгебри")
    await message.reply("Питання №1\nЧому дорівнює √144 ", reply_markup=reply_keyboards.algebra1)




@dp.message(Algebra.q1)
async def alg_q1(message: Message, state: FSMContext):
    result = '12'
    if message.text == result:
        await message.react([ReactionTypeEmoji(emoji="👍")])
        await message.reply('Правильна відповідь 😎', reply_markup=reply_keyboards.continue_kb1)
    else:
        await message.react([ReactionTypeEmoji(emoji="👎")])
        await message.reply("Помилка 🚨\nПравильна відповідь - 12", reply_markup=reply_keyboards.continue_kb1)
    await state.clear()



@dp.message(F.text == "Продовжити")
async def algebra_q2(message: Message, state: FSMContext):
    await state.set_state(Algebra.q2)
    await message.reply("Питання №2\n5 - 2 • 7 = ", reply_markup=reply_keyboards.algebra2)



@dp.message(Algebra.q2)
async def alg_q2(message: Message, state: FSMContext):

    result = '-3'
    if message.text == result:
        await message.react([ReactionTypeEmoji(emoji="👍")])
        await message.reply('+1 бал 😮‍💨', reply_markup=reply_keyboards.continue_kb2)

    else:
        await message.react([ReactionTypeEmoji(emoji="👎")])
        await message.reply(f"Неправильно 🚨\nПравильна відповідь - {result}", reply_markup=reply_keyboards.continue_kb2)



    await state.clear()




@dp.message(F.text == "Далі")
async def algebra_q3(message: Message, state: FSMContext):
    await state.set_state(Algebra.q3)
    await message.reply("Питання №3\n8² : 2 = ", reply_markup=reply_keyboards.algebra3)




@dp.message(Algebra.q3)
async def alg_q3(message: Message, state: FSMContext):

    result = '32'
    if message.text == result:
        await message.react([ReactionTypeEmoji(emoji="⚡️")])
        await message.reply('Правильно 👍🏻', reply_markup=reply_keyboards.continue_kb3)

    else:
        await message.react([ReactionTypeEmoji(emoji="🤬")])
        await message.reply(f"Ти помилився 😞\nПравильна відповідь - {result}", reply_markup=reply_keyboards.continue_kb3)



    await state.clear()


@dp.message(F.text == "Поїхали")
async def algebra_q4(message: Message, state: FSMContext):
    await state.set_state(Algebra.q4)
    await message.reply("Питання №4\n73% від 100 це", reply_markup=reply_keyboards.algebra4)


@dp.message(Algebra.q4)
async def alg_q2(message: Message, state: FSMContext):
    result = '73'
    if message.text == result:
        await message.react([ReactionTypeEmoji(emoji="⚡️")])
        await message.reply('Вірно 👍🏻', reply_markup=reply_keyboards.continue_kb4)
        
    else:
        await message.react([ReactionTypeEmoji(emoji="🤬")])
        await message.reply(f"Ти помилився\nПравильна відповідь - {result}", reply_markup=reply_keyboards.continue_kb4)

    await state.clear()


@dp.message(F.text == "Закінчити опитування")
async def end_q(message: Message):
    await message.reply("Вітаю ви пройшли тестування з алгебри!", reply_markup=inline_keyboards.go_menu)





@dp.message(F.text == "Географія")
async def p1(messge: Message, state: FSMContext):
    photo1 = FSInputFile("bot/images/newyork.jpg")
    await state.set_state(Geography.im1)
    await messge.answer_photo(photo1, "Вгадай який це город\nПідказка - це місто називают 'Місто, яке ніколи не засинає'")

@dp.message(Geography.im1)
async def enter_city1(message: Message, state: FSMContext):
    
    result = ["нью йорк", "ню йорк", "нью-йорк"]
    if message.text.lower() in result:
        await message.react([ReactionTypeEmoji(emoji="⚡️")])
        await message.reply('Правильно', reply_markup=reply_keyboards.cont_g1)
    else:
        await message.react([ReactionTypeEmoji(emoji="🖕")])
        await message.reply("Помилка, правильно відповідь - Нью Йорк", reply_markup=reply_keyboards.cont_g1)
    await state.clear()

@dp.message(F.text == "До наступного питання")
async def p2(message: Message, state: FSMContext):
    photo2 = FSInputFile('bot/images/berlin.jpg')
    await state.set_state(Geography.im2)
    await message.answer_photo(photo2,"Вгадай який це город\nПідказка - 'Це столиця найбільш населеної країни Європи'")



@dp.message(Geography.im2)
async def enter_city2(message: Message, state: FSMContext):
    
    result = "берлін"
    if message.text.lower() == result:
        await message.react([ReactionTypeEmoji(emoji="⚡️")])
        await message.reply('Ти крут!', reply_markup=reply_keyboards.cont_g2)
    else:
        await message.react([ReactionTypeEmoji(emoji="🖕")])
        await message.reply(f"Помилка, правильно відповідь - {result}", reply_markup=reply_keyboards.cont_g2)
    await state.clear()


@dp.message(F.text == "->")
async def p2(message: Message, state: FSMContext):
    photo3 = FSInputFile('bot/images/italy.jpg')
    await state.set_state(Geography.im3)
    await message.answer_photo(photo3,"Вгадай країну\nСхожа на сапог")


@dp.message(Geography.im3)
async def enter_country(message: Message, state: FSMContext):
    
    result = "італія"
    if message.text.lower() == result:
        await message.react([ReactionTypeEmoji(emoji="💘")])
        await message.reply('Ти крут!', reply_markup=reply_keyboards.cont_g3)
    else:
        await message.react([ReactionTypeEmoji(emoji="💩")])
        await message.reply(f"Помилка, правильно відповідь - {result}", reply_markup=reply_keyboards.cont_g3)
    await state.clear()



@dp.message(F.text == "Далі!!!")
async def p3(message: Message, state: FSMContext):
    await state.set_state(Geography.im4)
    await message.answer('Питання №4\nСтолиця Іспанії')


@dp.message(Geography.im4)
async def enter_country(message: Message, state: FSMContext):
    
    result = "мадрид"
    if message.text.lower() == result:
        await message.react([ReactionTypeEmoji(emoji="💘")])
        await message.reply('Правильно!', reply_markup=reply_keyboards.cont_g4)
    else:
        await message.react([ReactionTypeEmoji(emoji="💩")])
        await message.reply(f"Помилка, правильно відповідь - {result}", reply_markup=reply_keyboards.cont_g4)
    await state.clear()


@dp.message(F.text == "Завершити тест")
async def end_q1(message: Message):
    await message.reply("Вітаю ви пройшли тестування з географії!", reply_markup=inline_keyboards.go_menu)





@dp.message(F.text == "Перекладач")
async def _translator(message: Message, state: FSMContext):
    await state.set_state(Translate.msg)
    await message.reply("Починаємо перекладати, формат 🇺🇦 -> 🇬🇧")

@dp.message(Translate.msg)
async def _translate(message: Message, state: FSMContext):
    if message.text == "❌":
        await message.answer("Виберіть мод: ", reply_markup=reply_keyboards.subjects_kb)
        await state.finish()


    elif message.text == "🔄️":
        await state.set_state(Translate.msg)
        await message.reply("Введи текст: ")
    else:
        if message.text.startswith("Переклад : "):
            await message.reply(message.text, reply_markup=reply_keyboards.translator_kb)
        else:
            translated_text = translate_text(message.text, translator="google", from_language="uk", to_language="en")
            await message.reply("Переклад : " + translated_text, reply_markup=reply_keyboards.translator_kb)


@dp.callback_query(F.data=="go_home")
async def back(callback_query: CallbackQuery):
    await callback_query.message.reply('Повернення в головне меню ✅', reply_markup= reply_keyboards.subjects_kb)



@dp.message(F.text == "Контакт Розробника")
async def send_contact(message: Message):
    await message.answer_contact(phone_number="+380980195811", first_name="Льоня")


@dp.message(F.text == "Посилання на уроки")
async def links(message: Message):
    await message.reply(f'''
https://us05web.zoom.us/j/8452855547?pwd=b2xpZkNRM1hBZXFLdGRjbjVTbGNvdz09 - {hbold('Фізика / Інформатика')}\n
https://us05web.zoom.us/j/6536950820?pwd=ZGUwL1VZMHpWNnZTVDNQVWpTZEFwUT09- {hbold('Хімія')}\n
https://us05web.zoom.us/j/82300579633?pwd=kmx7RD3MGqhQqXapWO78nXpiwG8cWh.1- {hbold('Англійська')}\n
https://us05web.zoom.us/j/7500911710?pwd=UDhDcjlNclJpUjFZVW5aN3cxa1VvZz09 - {hbold('Фізкультура')}\n
https://us04web.zoom.us/j/5879157046?pwd=74WQImIHBsxUw6i86J3Ewq5ia9SyQZ.1 - {hbold('Зарубіжна література')}\n
https://us05web.zoom.us/j/7545658956?pwd=OE85SkFEZUJ5YzhXeVc3TVRYMXF5QT09 - {hbold('Труди')}\n
https://us04web.zoom.us/j/79501510803?pwd=VkhSUW50a01RdEo0QVlVZ0VIbzFZUT09 - {hbold('Німецька')}\n
https://us05web.zoom.us/j/7265907702?pwd=VkU3K05STTMzRk83YVRVOUg0c1VUUT09 - {hbold('Математика')}\n
https://zoom.us/j/94270252449?pwd=ZFhIRnBRUnoxbDJoTWROdU9tRWJ2UT09 - {hbold('Біологія')}\n
https://us04web.zoom.us/j/2127143372?pwd=LyCbyEfuJyYxNZCsricuHsYkyvUt1Q.1 - {hbold('Географія')}\n
''')



async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())