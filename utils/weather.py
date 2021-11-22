import datetime

import requests
from aiogram.utils.markdown import hunderline, hbold

forecast_weather = []

date = datetime.datetime.now().strftime('%d.%m.%Y')

weather_api = '0d4982c5dacd84aae707350da54a6043'


async def weather(city='Краснодар', weather_api=weather_api):
    code_to_smile = {
        "Clear": "\U00002600 Ясно",
        "Clouds": "\U00002601 Облачно",
        "Rain": "\U00002614 Дождь",
        "Drizzle": "\U00002614 Дождь",
        "Thunderstorm": "\U000026A1 Гроза",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    data_weather = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api}&units=metric').json()

    weather_description = data_weather['weather'][0]['main']

    if weather_description in code_to_smile:
        wd = code_to_smile[weather_description]
    else:
        wd = 'Высунь ебало на улицу и сам посмотри'

    city = data_weather['name']
    feels_like = round(data_weather['main']['feels_like'])
    temp = round(data_weather['main']['temp'])
    temp_max = round(data_weather['main']['temp_max'])
    temp_min = round(data_weather['main']['temp_min'])
    humidity = data_weather['main']['humidity']
    sunrise = datetime.datetime.fromtimestamp(data_weather['sys']['sunrise'])
    sunset = datetime.datetime.fromtimestamp(data_weather['sys']['sunset'])
    forecast = (f'*** {hbold(city)} - {hbold(date)} ***\n'
                          f'️{hunderline(wd)}\n'
                          f'🌡️ {hunderline("Температура")} {hbold(temp)}℃\n'
                          f'🌡️ {hunderline("Ощущается как")}  {hbold(feels_like)}℃\n'
                          f'🌡️ {hunderline("Максимальная температура")}  {hbold(temp_max)}℃\n'
                          f'🌡️ {hunderline("Минимальная температура")}  {hbold(temp_min)}℃\n'
                          f'💧 {hunderline("Влажность")} - {hbold(humidity)}%\n'
                          f'🌅 {hunderline("Рассвет")} - {hbold(sunrise.strftime("%H:%M"))}\n'
                          f'🌇 {hunderline("Закат")} - {hbold(sunset.strftime("%H:%M"))}')
    forecast_weather.append(forecast)