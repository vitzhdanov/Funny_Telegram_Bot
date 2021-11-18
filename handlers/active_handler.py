from aiogram import types
from loader import dp
from random import choice
from aiogram.utils.markdown import hitalic, hcode, hunderline, italic

count = []


@dp.message_handler()
async def check_active(message: types.Message):
    if str(message.chat.id) not in str(count):
        count.append(
            {
                message.chat.id: 1
            }
        )
    else:
        [chat for chat in count if str(message.chat.id) in str(chat)][0][message.chat.id] += 1
    print(count)


async def send_pic():
    gifs =[
        'https://i.gifer.com/origin/3f/3fcf565ccc553afcfd89858c97304705.gif',
        'https://i.gifer.com/WoG5.gif',
    ]
    if len(count) > 0:
        for chat in count:
            for k, v in chat.items():
                if v == 0:
                    # await dp.bot.send_message(chat_id=k, text='swswsw')
                    await dp.bot.send_video(chat_id=k, video=choice(gifs))
                else:
                    [chat for chat in count if str(k) in str(chat)][0][k] = 0
    print(count)