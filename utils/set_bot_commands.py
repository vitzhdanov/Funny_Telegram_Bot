from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("lucky", "Проверь удачу"),
            types.BotCommand("weather", "Погода"),
            types.BotCommand("help", "Узнай скрытые возможности"),
        ]
    )
