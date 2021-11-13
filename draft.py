from data.config import data

from aiogram import types
from loader import dp
import psycopg2
from aiogram.dispatcher import filters
from datetime import datetime

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
        create = """DROP TABLE user_phrases;"""
        cursor.execute(create)
        print('Table created')

except Exception as ex:
    print(f'[INFO] - {ex}')
finally:
    if connection:
        print('Connection close')
        connection.close()