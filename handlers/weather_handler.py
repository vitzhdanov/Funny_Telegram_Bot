from aiogram import types
from loader import dp
from utils.weather import forecast_weather


# Погода
@dp.message_handler(commands='weather')
async def weather_handler(message: types.Message):
    await message.answer(forecast_weather[0])
    await dp.bot.delete_message(message.chat.id, message.message_id)
