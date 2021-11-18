from aiogram import types
from loader import dp

lst_user = []


@dp.message_handler(commands='lucky')
async def luck(message: types.Message):
    await message.delete()
    mes = await dp.bot.send_dice(chat_id=message.chat.id)
    chat_id = str(message.chat.id).replace('-', '')
    user_id = str(message.from_user.id).replace('-', '')
    # добавляю юзера если его нет в списке
    if f'{chat_id}: {chat_id}: {user_id}' not in str([user for user in lst_user]).replace("'", ''):
        lst_user.append(
            {
                chat_id: f'{chat_id}: {user_id}',
                'name': message.from_user.first_name or message.from_user.username,
                'value': mes['dice']['value']
            }
        )
    print(lst_user)
    # print(f'{chat_id}: {chat_id}: {user_id}')
    # Если количество уникальных юзеров больше одного запускаем эту логику
    if len(lst_user) > 1:
        # Находим самое большое значение
        # max_val = [i for i in lst_user if i['value'] == max([i['value'] for i in lst_user])]
        max_val = []
        for user in lst_user:
            for k, v in user.items():
                if k == chat_id:
                    max_val.append(
                        {
                            'name': user['name'],
                            'chat_id': chat_id,
                            'value': user['value']
                        }
                    )
        # Если самое большое значение одно
        print(max_val)
        if len([i for i in max_val if i['chat_id'] == chat_id]) == 1:
            await message.answer(f"{''.join([i['name'] for i in max_val])} доминирует над {[user for user in lst_user if user!=max_val[0]][0]['name']}")
            lst_user.clear()
        # Если два значения одинаковые
        elif len([i for i in max_val if i['chat_id'] == chat_id]) > 1:
            await message.answer(f"Победила дружба {' и '.join([i['name'] for i in max_val])}")
            lst_user.clear()