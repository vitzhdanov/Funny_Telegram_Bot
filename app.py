import asyncio

from aiogram import executor
import aioschedule

from loader import dp
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from utils.horoscope import horoscope

from utils.phrase_of_the_day import phrase_day
from handlers.active_handler import list_chat
from utils.mn_wd_fr import day_pic


async def phrase_of_the_day():
    for chat in list_chat:
        await dp.bot.send_message(text=phrase_day(), chat_id=chat)


async def day_picture():
    for chat in list_chat:
        await dp.bot.send_photo(photo=day_pic(), chat_id=chat)


async def scheduler():
    aioschedule.every().day.at("00:01").do(horoscope)
    aioschedule.every().day.at("08:33").do(phrase_of_the_day)
    aioschedule.every().monday.at("07:30").do(day_picture)
    aioschedule.every().wednesday.at("07:30").do(day_picture)
    aioschedule.every().friday.at("07:30").do(day_picture)

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

