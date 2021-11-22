import requests
from aiogram import types
from bs4 import BeautifulSoup
from loader import dp


# Отправляет запрос на вебсирвис по генерации случайных советов
@dp.message_handler(commands='advice')
async def advice(message: types.Message):
    await message.delete()
    req = requests.get('https://www.randomes.top/besplatnyy-generator-sovetov/').text
    soup = BeautifulSoup(req, 'lxml')
    advice = soup.find('div', class_='wpb_raw_code').find('span').text
    await message.answer(f"{message.from_user.first_name.capitalize() or message.from_user.username.capitalize()}, {advice.lower()}")
