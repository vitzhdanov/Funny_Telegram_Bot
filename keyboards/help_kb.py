from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Клавиатура для хендлера помощи
help_kb = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [
        InlineKeyboardButton(text='Поиск Google', switch_inline_query_current_chat='Бот поиск '),
    ],
    [
        InlineKeyboardButton(text='Красивый URL', switch_inline_query_current_chat='Бот обрежь ссылку '),
    ],
    [
        InlineKeyboardButton(text='Сохранить слово/фразу', switch_inline_query_current_chat='Бот сохрани '),
    ],
    [
        InlineKeyboardButton(text='Вывести все фразы', switch_inline_query_current_chat='Бот покажи фразы'),
    ],
])