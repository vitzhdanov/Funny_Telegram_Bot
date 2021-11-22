from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


help_kb = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [
        InlineKeyboardButton(text='Поиск Google', switch_inline_query_current_chat='Бот поиск '),
    ],
    [
        InlineKeyboardButton(text='Сохранить слово/фразу', switch_inline_query_current_chat='Бот сохрани '),
    ],
    [
        InlineKeyboardButton(text='Вывести все фразы', switch_inline_query_current_chat='Бот покажи фразы'),
    ],
])