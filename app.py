import asyncio

from aiogram import executor
import aioschedule
from random import choice
from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def star_of_the_day():
    await dp.bot.send_message(text=f"👏 {choice(['Владислав', 'Ярослав', 'Александр'])} сегодня ты способен на всё!🤙", chat_id=495432329)


async def scheduler():
    aioschedule.every().day.at("7:00").do(star_of_the_day)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)

    asyncio.create_task(scheduler())


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

