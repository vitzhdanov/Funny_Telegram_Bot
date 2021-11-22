import requests
from aiogram import types
from loader import dp


@dp.message_handler(commands='yesno')
async def decision(message: types.Message):
    response = requests.get('https://yesno.wtf/api').json()['image']
    await dp.bot.send_video(chat_id=message.chat.id, video=response)
