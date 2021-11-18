from aiogram import types
from aiogram.dispatcher import filters
from loader import dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.callback_data import CallbackData

SAVE_WORD = ['Бот', 'поиск']


@dp.message_handler(filters.Text(contains=SAVE_WORD))
async def test(message: types.Message):
    text = message.text.replace('Бот поиск ', '').replace('@zed_is_dead_bot', '').replace(' ', '+')
    google_callback = CallbackData('choose', 'req')
    google_key = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='🔍', callback_data=google_callback.new(req='req'), url=f'https://www.google.com/search?q={text}')
        ]
    ])
    await message.answer(text='🥸', reply_markup=google_key)