from aiogram import types
from aiogram.dispatcher import filters
from loader import dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.callback_data import CallbackData

lst_user = []

SAVE_WORD = ['бот', 'поиск']


@dp.message_handler(filters.Text(contains=SAVE_WORD))
async def test(message: types.Message):
    text = message.text.replace('бот поиск ', '').replace(' ', '+')
    google_callback = CallbackData('choose', 'req')
    google_key = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='🔍', callback_data=google_callback.new(req='req'), url=f'https://www.google.com/search?q={text}')
        ]
    ])
    await message.answer(text='🥸', reply_markup=google_key)


@dp.message_handler(text='/lucky')
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
    print(message.chat.id)
    if len(lst_user) > 1:
        c = [i for i in lst_user if i['value'] == max([i['value'] for i in lst_user])]
        if len(c) == 1:
            await message.answer(f"{''.join([i['name'] for i in c])} обыграл и уничтожил")
            lst_user.clear()
        elif len(c) > 1:
            await message.answer(f"Победила дружба {' и '.join([i['name'] for i in c])}")
            lst_user.clear()


@dp.edited_message_handler()
async def mes(message: types.Message):
    await message.reply('Будьте на чеку, сообщение изменено...')
