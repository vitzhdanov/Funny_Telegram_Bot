import time

from aiogram import types
from loader import dp

lst_user = []


@dp.message_handler(commands='lucky')
async def luck(message: types.Message):

    mes = await dp.bot.send_dice(chat_id=message.chat.id)
    chat_id = str(message.chat.id).replace('-', '')
    user_id = str(message.from_user.id).replace('-', '')
    # Если ID чата нет то добавляем
    if chat_id not in str(set().union(*(d.keys() for d in lst_user))):
        lst_user.append(
            {
                chat_id: [{
                    'id': user_id,
                    'name': message.from_user.first_name or message.from_user.username,
                    'value': mes['dice']['value']
                }]
            }
        )
        print(lst_user)
    # Если ID чата добавлен, проверяем нет ли юзера в этом словаре, если нет то добавляем
    else:
        users_in_chat = [i for i in lst_user if chat_id in i.keys()][0][chat_id]
        print(users_in_chat)
        print(user_id)
        print(set().union(*(k.values() for k in users_in_chat)))
        if user_id not in set().union(*(k.values() for k in users_in_chat)):
            users_in_chat.append(
                {
                    'id': user_id,
                    'name': message.from_user.first_name or message.from_user.username,
                    'value': mes['dice']['value']
                }
            )
            # Ищем самое большое значение в текущем чате
            winner = [i for i in users_in_chat if i['value'] == max(i['value'] for i in users_in_chat)]
            # Если значение одно
            if len(winner) == 1:
                time.sleep(3)
                await message.answer(f"Удача на стороне - {winner[0]['name']}")
                lst_user.remove([i for i in lst_user if chat_id in i.keys()][0])
            # Если значений два, ничья
            else:
                time.sleep(3)
                await message.answer(f"Победила дружба {' и '.join([i['name'] for i in winner])}")
                lst_user.remove([i for i in lst_user if chat_id in i.keys()][0])