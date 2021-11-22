from aiogram import types
from loader import dp
from random import choice
from datetime import datetime

count = []
list_chat = []


# Проверяет активность в чате
@dp.message_handler()
async def check_active(message: types.Message):
    if message.chat.id not in list_chat:
        list_chat.append(message.chat.id)
    if str(message.chat.id) not in str(count):
        count.append(
            {
                message.chat.id: 1
            }
        )
    else:
        [chat for chat in count if str(message.chat.id) in str(chat)][0][message.chat.id] += 1



async def send_pic():
    gifs =[
        'https://i.gifer.com/origin/3f/3fcf565ccc553afcfd89858c97304705.gif',
        'https://i.gifer.com/WoG5.gif',
    ]
    stop_hours = [23, 00, 1, 2, 3, 4, 5, 6, 7]
    if datetime.now().hour not in stop_hours:
        if len(count) > 0:
            for chat in count:
                for k, v in chat.items():
                    if v == 0:
                        await dp.bot.send_video(chat_id=k, video=choice(gifs))
                    else:
                        [chat for chat in count if str(k) in str(chat)][0][k] = 0
    else:
        pass

