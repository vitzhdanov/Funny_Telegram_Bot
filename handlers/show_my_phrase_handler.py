from data.config import data

from aiogram import types
from loader import dp
import psycopg2
from aiogram.dispatcher import filters

SAVE_WORD = ['Бот', 'покажи мои', 'фраз']


@dp.message_handler(filters.Text(contains=SAVE_WORD))
async def phrases(message: types.Message):
    user_id = message.from_user.id

    try:
        connection = psycopg2.connect(
            host=data['host'],
            user=data['user'],
            database=data['database'],
            port=data['port'],
            password=data['password'],
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            command_select = """SELECT user_phrase FROM user_phrases_%s WHERE user_id=%s;"""
            cursor.execute(command_select, (int(str(message.chat.id).replace('-','')), user_id,))
            list_phrases = []
            for phrase in cursor.fetchall():
                list_phrases.append(phrase[0])
            await message.answer('\n'.join(list_phrases))

    except Exception as ex:
        print(f'[INFO] - {ex}')
    finally:
        if connection:
            print('Connection close')
            connection.close()