from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from callback_data import type_horo


kb_horoscope = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(text='Общий', callback_data=type_horo.new(type='general')),
        InlineKeyboardButton(text='Бизнес', callback_data=type_horo.new(type='business')),
        InlineKeyboardButton(text='Эротический', callback_data=type_horo.new(type='erotic')),
        InlineKeyboardButton(text='Здоровья', callback_data=type_horo.new(type='health')),
        InlineKeyboardButton(text='Кулинарный', callback_data=type_horo.new(type='cooking')),
        InlineKeyboardButton(text='Любовный', callback_data=type_horo.new(type='love')),
    ]
])

sign_zodiac = InlineKeyboardMarkup(row_width=4, inline_keyboard=[
    [
        InlineKeyboardButton(text='Овен', callback_data='aries'),
        InlineKeyboardButton(text='Телец', callback_data='taurus'),
        InlineKeyboardButton(text='Близнецы', callback_data='gemini'),
        InlineKeyboardButton(text='Рак', callback_data='cancer'),
        InlineKeyboardButton(text='Лев', callback_data='leo'),
        InlineKeyboardButton(text='Дева', callback_data='virgo'),
        InlineKeyboardButton(text='Весы', callback_data='libra'),
        InlineKeyboardButton(text='Скорпион', callback_data='scorpio'),
        InlineKeyboardButton(text='Стрелец', callback_data='sagittarius'),
        InlineKeyboardButton(text='Козерог', callback_data='capricorn'),
        InlineKeyboardButton(text='Водолей', callback_data='aquarius'),
        InlineKeyboardButton(text='Рыбы', callback_data='pisces'),
    ]
])