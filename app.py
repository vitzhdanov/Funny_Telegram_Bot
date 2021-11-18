import asyncio

from aiogram import executor
import aioschedule
from random import choice
from loader import dp
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from utils.horoscope import horoscope
from handlers.active_handler import send_pic
from handlers.count_fword_handler import record_fword, display_fword
from utils.


async def star_of_the_day():
    await dp.bot.send_message(text=f"👏 {choice(['Владислав', 'Ярослав', 'Александр'])} сегодня ты способен на всё!🤙", chat_id=495432329)


async def phrase_of_the_day():
    await dp.bot.send_message()

async def scheduler():
    aioschedule.every().day.at("7:00").do(star_of_the_day)
    aioschedule.every().day.at("00:01").do(horoscope)
    aioschedule.every(2).hours.do(send_pic)
    aioschedule.every().hour.do(record_fword)
    aioschedule.every().day.at("21:00").do(display_fword)
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

