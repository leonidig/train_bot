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



router = Router()


@router.message(F.text == "Basketball")
async def test_btn(message: Message):
    await message.answer_dice('🏀')

@router.message(F.text == "Dice")
async def test_btn(message: Message):
    await message.answer_dice('🎲')


@router.message(F.text == "Casino")
async def test_btn(message: Message):
    await message.answer_dice('🎰')


@router.message(F.text == "Football")
async def test_btn(message: Message):
    await message.answer_dice('⚽️')