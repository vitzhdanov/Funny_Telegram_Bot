from aiogram import types
from loader import dp

lst_user = []


@dp.message_handler(commands='lucky')
async def luck(message: types.Message):
    await message.delete()
    mes = await dp.bot.send_dice(chat_id=message.chat.id)
    # добавляю юзера если его нет в списке
    if message.from_user.id not in [user['id'] for user in lst_user]:
        lst_user.append(
            {
                'id': message.from_user.id,
                'name': message.from_user.first_name or message.from_user.username,
                'value': mes['dice']['value']
            }
        )
    # Если количество уникальных юзеров больше одного запускаем эту логику
    if len(lst_user) > 1:
        # Находим самое большое значение
        max_val = [i for i in lst_user if i['value'] == max([i['value'] for i in lst_user])]
        # Если самое большое значение одно
        if len(max_val) == 1:
            await message.answer(f"{''.join([i['name'] for i in max_val])} доминирует над {[user for user in lst_user if user!=max_val[0]][0]['name']}")
            lst_user.clear()
        # Если два значения одинаковые
        elif len(max_val) > 1:
            await message.answer(f"Победила дружба {' и '.join([i['name'] for i in max_val])}")
            lst_user.clear()