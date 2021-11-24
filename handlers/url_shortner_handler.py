from aiogram import types
from aiogram.dispatcher import filters
from loader import dp
import requests
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.callback_data import CallbackData

SHORTNER_WORD = ['Бот', 'обрежь', 'ссылку']


# укорачивает ссылку
@dp.message_handler(filters.Text(contains=SHORTNER_WORD))
async def test(message: types.Message):
    user_link = message.text.replace('Бот обрежь ссылку ', '').replace('@zed_is_dead_bot', '').split()
    resp = requests.post('https://www.iclc.info/shortner/', {'long_url': str(user_link)}).json()
    sym = str(resp['short_sym'])
    em = resp['short_em']
    shortner_key = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=sym, switch_inline_query_current_chat=sym)
        ],
        [
            InlineKeyboardButton(text=em, switch_inline_query_current_chat=em)
        ]
    ])
    # await message.answer(f"{user_link}\n{sym}\n\n{em}")
    await message.answer('r', reply_markup=shortner_key)