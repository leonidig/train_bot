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
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.markdown import hbold
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReactionTypeEmoji


from keyboards import reply_keyboards, inline_keyboards
from commands import commands_router
from utils.states import Algebra





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
    
    if message.text.lower() == "12":
        await message.react([ReactionTypeEmoji(emoji="👍")])
        await message.reply('Правильна відповідь 😎', reply_markup=reply_keyboards.continue_kb1)
        
    else:
        await message.react([ReactionTypeEmoji(emoji="👎")])
        await message.reply("Помилка 🚨", reply_markup=reply_keyboards.continue_kb1)
        


    await state.clear()



@dp.message(F.text == "Продовжити")
async def algebra_q2(message: Message, state: FSMContext):
    await state.set_state(Algebra.q2)
    await message.reply("Питання №2\n5 - 2 • 7 = ", reply_markup=reply_keyboards.algebra2)



@dp.message(Algebra.q2)
async def alg_q2(message: Message, state: FSMContext):

    if message.text == "-3":
        await message.react([ReactionTypeEmoji(emoji="👍")])
        await message.reply('+1 бал 😮‍💨', reply_markup=reply_keyboards.continue_kb2)

    else:
        await message.react([ReactionTypeEmoji(emoji="👎")])
        await message.reply("Неправильно 🚨", reply_markup=reply_keyboards.continue_kb2)



    await state.clear()




@dp.message(F.text == "Далі")
async def algebra_q3(message: Message, state: FSMContext):
    await state.set_state(Algebra.q3)
    await message.reply("Питання №3\n8² : 2 = ", reply_markup=reply_keyboards.algebra3)




@dp.message(Algebra.q3)
async def alg_q2(message: Message, state: FSMContext):

    if message.text == "32":
        await message.react([ReactionTypeEmoji(emoji="⚡️")])
        await message.reply('Правильно 👍🏻', reply_markup=reply_keyboards.continue_kb3)

    else:
        await message.react([ReactionTypeEmoji(emoji="🤬")])
        await message.reply("Ти помилився 😞", reply_markup=reply_keyboards.continue_kb3)



    await state.clear()


@dp.message(F.text == "Поїхали")
async def algebra_q4(message: Message, state: FSMContext):
    await state.set_state(Algebra.q4)
    await message.reply("Питання №4\n73% від 100 це", reply_markup=reply_keyboards.algebra4)


@dp.message(Algebra.q4)
async def alg_q2(message: Message, state: FSMContext):
    if message.text == "73":
        await message.react([ReactionTypeEmoji(emoji="⚡️")])
        await message.reply('Вірно 👍🏻', reply_markup=reply_keyboards.continue_kb4)
        
    else:
        await message.react([ReactionTypeEmoji(emoji="🤬")])
        await message.reply("Ти помилився", reply_markup=reply_keyboards.continue_kb4)

    await state.clear()


@dp.message(F.text == "Закінчити опитування")
async def end_q(message: Message):
    await message.reply("Вітаю ви пройшли тестування з алгебри!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())