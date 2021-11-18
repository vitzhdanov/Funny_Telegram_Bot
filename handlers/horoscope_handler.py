import json
from aiogram.utils.markdown import hunderline, hitalic
from loader import dp
from aiogram import types
from aiogram.types import CallbackQuery
from keyboards.horoscope_kb import kb_horoscope, sign_zodiac
from keyboards.callback_data import type_horo, zodiac
import codecs

type_h = []


@dp.message_handler(commands='horoscope')
async def type_horoscope(message: types.Message):
    choose = hunderline('Чтобы ты хотел узнать?😈').center(22)
    await message.answer(text=choose, reply_markup=kb_horoscope)
    await dp.bot.delete_message(message.chat.id, message.message_id)


@dp.callback_query_handler(type_horo.filter(type=['general', 'business', 'erotic', 'health', 'cooking', 'love']))
async def general(call: CallbackQuery):
    choose = hunderline('♑️ Выбери знак ♈️').center(22)
    await call.message.answer(text=choose, reply_markup=sign_zodiac)
    hor = call.data.replace('horoscope:', '')
    global type_h
    type_h.append(hor)
    await call.message.edit_reply_markup()


@dp.callback_query_handler(zodiac.filter(zodiac=['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']))
async def display(call: CallbackQuery):
    global type_h
    sign = call.data.replace('sign:', '')
    with codecs.open(f'utils/horoscopes/{type_h.pop()}.json', 'r', 'utf_8_sig') as file:
        horoscope = json.load(file)
    text = f"{hunderline('Гороскоп на ')}{horoscope['horo']['date']['@today']}\n" \
           f"{hitalic(horoscope['horo'][sign]['today'])}"
    await call.message.answer(text=text)
    await call.message.edit_reply_markup()