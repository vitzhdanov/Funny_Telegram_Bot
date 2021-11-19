import time

from aiogram import types
from loader import dp

lst_user = []


@dp.message_handler(commands='lucky')
async def luck(message: types.Message):

    mes = await dp.bot.send_dice(chat_id=message.chat.id)
    chat_id = str(message.chat.id).replace('-', '')
    user_id = str(message.from_user.id).replace('-', '')
    # добавляю юзера если его нет в списке
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
            winner = [i for i in users_in_chat if i['value'] == max(i['value'] for i in users_in_chat)]

            if len(winner) == 1:
                time.sleep(3)
                await message.answer(f"Удача на стороне - {winner[0]['name']}")
                lst_user.remove([i for i in lst_user if chat_id in i.keys()][0])
                    # print(lst_user)
            else:
                time.sleep(3)
                await message.answer(f"Победила дружба{' и '.join([i['name'] for i in winner])}")
                lst_user.remove([i for i in lst_user if chat_id in i.keys()][0])
        #         print(lst_user)
        # else:
        #     try:
        #         winner = [i for i in users_in_chat if i['value'] == max(i['value'] for i in users_in_chat)]
        #         if len(winner) == 1:
        #             print(f"Winner - {winner[0]['name']}")
        #             users_in_chat.remove([i for i in users_in_chat if chat_id in i.keys()][0])
        #             print(users_in_chat)
        #         else:
        #             print(' и '.join([i['name'] for i in winner]))
        #             users_in_chat.remove([i for i in users_in_chat if chat_id in i.keys()][0])
        #             print(users_in_chat)
        #     except IndexError:
        #         pass
    #

    #
    #
    #
    # if chat_id not in str(list(set().union(*(k.keys() for k in lst_user)))):
    #     lst_user.append(
    #         {
    #             chat_id: [
    #                 {
    #                     'id': user_id,
    #                     'name': message.from_user.first_name or message.from_user.username,
    #                     'value': mes['dice']['value']
    #                 }
    #             ]
    #         }
    #     )
    # else:
    #     for chat in lst_user:
    #         if user_id not in str(chat.items()):
    #             chat[chat_id].append(
    #                 {
    #                     'id': user_id,
    #                     'name': message.from_user.first_name or message.from_user.username,
    #                     'value': mes['dice']['value']
    #                 }
    #             )
    # print(lst_user)
    # # print(f'{chat_id}: {chat_id}: {user_id}')
    # # Если количество уникальных юзеров больше одного запускаем эту логику
    # for chat in lst_user:
    #     try:
    #         if len(chat[chat_id]) > 1:
    #         # Находим самое большое значение
    #             max_val = [i for i in chat[chat_id] if i['value'] == max([i['value'] for i in chat[chat_id]])]
    #
    #             print(max_val)
    #             if len(max_val) == 1:
    #                 print(max_val)
    #                 await message.answer(f"{[i['name'] for i in max_val][0]} доминирует")
    #                 lst_user.clear()
    #             # Если два значения одинаковые
    #             elif len(max_val)==2:
    #                 await message.answer(f"Победила дружба {' и '.join([i['name'] for i in max_val])}")
    #                 lst_user.clear()
    #     except KeyError:
    #         pass