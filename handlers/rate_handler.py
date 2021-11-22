from aiogram import types
from aiogram.utils.markdown import hunderline

from utils.rate import *
from loader import dp, bot
from aiogram.types import CallbackQuery

from datetime import datetime


# Курс валют
@dp.message_handler(commands='rate')
async def rates(message:types.Message):
    date = datetime.now().strftime('%d.%m.%Y')
    choose = hunderline(f'💱 Курс валют на {date} 💹').center(22)
    await message.answer(text=choose, reply_markup=key)
    await bot.delete_message(message.chat.id, message.message_id)


@dp.callback_query_handler(data.filter())
async def close(call: CallbackQuery):
    await call.message.edit_reply_markup()