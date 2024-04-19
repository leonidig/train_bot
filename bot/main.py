import asyncio
import logging
import sys
from os import getenv, listdir, path
from dotenv import load_dotenv


from aiogram import Bot, Dispatcher, html, Router, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.markdown import hbold
from aiogram.types import Message



from keyboards import reply_keyboards, inline_keyboards
from commands import commands_router




load_dotenv()
print(getenv("TOKEN"))
TOKEN = getenv("TOKEN")



router = Router()
dp = Dispatcher()
dp.include_router(commands_router)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=reply_keyboards.main_kb)




async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())