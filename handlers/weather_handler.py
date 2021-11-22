from aiogram import types
from loader import dp
from utils.weather import forecast_weather


@dp.message_handler(commands='weather')
async def weather_handler(message: types.Message):
    await message.answer(forecast_weather[0])
