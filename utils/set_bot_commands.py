from datetime import datetime
from aiogram import types

date = datetime.now().strftime('%d.%m.%Y')


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("horoscope", f'Гороскоп на {date} 💫'),
            types.BotCommand("weather", f'Погода на {date} ☔️'),
            types.BotCommand('rate', f'Курс валют на {date} 💱'),
            types.BotCommand("lucky", "Проверь удачу 🍀"),
            types.BotCommand("advice", "Совет от Бота 🤖"),
            types.BotCommand("yesno", "Бот решит за тебя: ✅ или ❌"),
            types.BotCommand("help", "Узнай скрытые возможности 📔"),
        ]
    )
