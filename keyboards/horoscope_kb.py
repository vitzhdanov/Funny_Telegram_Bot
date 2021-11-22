from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback_data import type_horo, zodiac

# Клавиатура для гороскопа
kb_horoscope = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(text='Общий ✨', callback_data=type_horo.new(type='general')),
        InlineKeyboardButton(text='Бизнес 🏢', callback_data=type_horo.new(type='business')),
        InlineKeyboardButton(text='Эротический 🔥', callback_data=type_horo.new(type='erotic'))
    ],
    [
        InlineKeyboardButton(text='Здоровья 💉', callback_data=type_horo.new(type='health')),
        InlineKeyboardButton(text='Кулинарный 🍳', callback_data=type_horo.new(type='cooking')),
        InlineKeyboardButton(text='Любовный ❤️', callback_data=type_horo.new(type='love')),
    ]
])

sign_zodiac = InlineKeyboardMarkup(row_width=4, inline_keyboard=[
    [
        InlineKeyboardButton(text='Овен ♈', callback_data=zodiac.new(zodiac='aries')),
        InlineKeyboardButton(text='Телец ♉', callback_data=zodiac.new(zodiac='taurus')),
        InlineKeyboardButton(text='Близнецы ♊', callback_data=zodiac.new(zodiac='gemini')),
    ],
    [
        InlineKeyboardButton(text='Рак ♋', callback_data=zodiac.new(zodiac='cancer')),
        InlineKeyboardButton(text='Лев ♌', callback_data=zodiac.new(zodiac='leo')),
        InlineKeyboardButton(text='Дева ♍', callback_data=zodiac.new(zodiac='virgo')),
    ],
    [
        InlineKeyboardButton(text='Весы ♎', callback_data=zodiac.new(zodiac='libra')),
        InlineKeyboardButton(text='Скорпион ♏', callback_data=zodiac.new(zodiac='scorpio')),
        InlineKeyboardButton(text='Стрелец ♐', callback_data=zodiac.new(zodiac='sagittarius')),
    ],
    [
        InlineKeyboardButton(text='Козерог ♑', callback_data=zodiac.new(zodiac='capricorn')),
        InlineKeyboardButton(text='Водолей ♒', callback_data=zodiac.new(zodiac='aquarius')),
        InlineKeyboardButton(text='Рыбы ♓', callback_data=zodiac.new(zodiac='pisces')),
    ]
])