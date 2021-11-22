from aiogram import types
from loader import dp
from aiogram.utils.markdown import hitalic, hcode, hunderline, italic
from keyboards.help_kb import help_kb


# Показывает возможности бота
@dp.message_handler(commands='help')
async def help_func(message: types.Message):
    text = (f"{hunderline('Бот поиск ')}{hcode('*запрос*')} - {hitalic('поиск в гугле.')}\n"
            f"{hunderline('Бот сохрани ')}{hcode('*слово/фраза*')} - {hitalic('сохраняет в БД.')}\n"
            f"{hunderline('Бот покажи фразы')} - {hitalic('выводит все сохранённые фразы.')}\n"
            f"{hunderline('Бот покажи мои фразы')} - {hitalic('выводит сохранённые вами фразы.')}\n")
    await message.answer(text=text, reply_markup=help_kb)


# Отслеживает редактирование сообщений
@dp.edited_message_handler()
async def mes(message: types.Message):
    await message.reply('Будьте на чеку, сообщение изменено...')
