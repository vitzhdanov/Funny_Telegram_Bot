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
from utils.weather import weather


# Если чат активен отправляет фразу дня
async def phrase_of_the_day():
    for chat in list_chat:
        await dp.bot.send_message(text=phrase_day(), chat_id=chat)


# Если чат активен отправляет картинку
async def day_picture():
    for chat in list_chat:
        await dp.bot.send_photo(photo=day_pic(), chat_id=chat)


async def clear_list_chat():
    list_chat.clear()


async def scheduler():
    # Запрос на погоду в указанное время
    aioschedule.every().minute.do(clear_list_chat)
    # aioschedule.every().wednesday.at("20:00").do()
    # Запрос на гороскоп в указанное время
    aioschedule.every().day.at("21:20").do(horoscope)
    # Каждый день в указанное время выводит фразу дня
    aioschedule.every().day.at("05:02").do(phrase_of_the_day)
    # Каждый понедельник, среду, пятницу выводит картинку
    aioschedule.every().monday.at("05:00").do(day_picture)
    aioschedule.every().wednesday.at("05:00").do(day_picture)
    aioschedule.every().friday.at("05:00").do(day_picture)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)

    # При запуске отправляет запрос на прогноз погоды

    # При запуске отправляет запрос на гороскоп
    await horoscope()

    asyncio.create_task(scheduler())


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

