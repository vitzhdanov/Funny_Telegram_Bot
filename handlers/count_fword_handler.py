from aiogram import types
from aiogram.dispatcher import filters
from loader import dp
from aiogram.utils.markdown import hitalic, hcode, hunderline
import psycopg2
from data.config import data


F_WORDS = ['бля', 'пизд', 'еба', 'ебу', 'долб', 'далб', 'гондон', 'гандон', 'пидар', 'пидор', 'пздц', 'хуй', 'хуя', 'хуе', 'хуи', 'хули']
# Local count fwords
count = []


@dp.message_handler(commands='fwords')
async def show_fwords(message: types.Message):
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
            create = '''SELECT * FROM fwords;'''
            cursor.execute(create)
        await message.answer(cursor.fetchall)

    except Exception as ex:
        print(f'[INFO] - {ex}')
    finally:
        if connection:
            print('Connection close')
            connection.close()


@dp.message_handler()
async def f_word(message: types.Message):
    global count
    text = message.text.lower()
    for word in F_WORDS:
        if word in text:
            if str(message.from_user.id) not in str(count):
                count.append(
                    {
                        'id': message.from_user.id,
                        'user': message.from_user.first_name or message.from_user.username,
                        'count': 0
                    }
                )
            [user for user in count if user['id'] == message.from_user.id][0]['count'] += text.count(word)
            print(count)


async def record_fword():
    # If count doesn't empty, we are connect
    if len(count) > 0:
        try:
            connection = psycopg2.connect(
                host=data['host'],
                user=data['user'],
                database=data['database'],
                port=data['port'],
                password=data['password'],
            )
            connection.autocommit = True

            # Create table if not exists
            with connection.cursor() as cursor:
                create = """CREATE TABLE IF NOT EXISTS fwords (
                                id serial PRIMARY KEY, 
                                user_id int NOT NULL,
                                user_name varchar(100),
                                count int);"""
                cursor.execute(create)
                print('Table created')

                # Insert data
                with connection.cursor() as cursor:
                    insert_command = """INSERT INTO fwords (user_id, user_name, count) VALUES (%s, %s, %s);"""
                    cursor.execute("""SELECT user_id from fwords;""")
                    for user in count:
                        # If user already inserted, we are update his count and clear local count
                        if str(user['id']) in str(cursor.fetchall()):
                            cursor.execute("""UPDATE fwords SET count = count + %s WHERE user_id = %s""", (user['count'], user['id']))
                            user['count'] = 0
                            print(f'Update {user["user"]} success')
                        # If user doesn't exists, we are insert user and clear his count
                        else:
                            cursor.execute(insert_command, (user['id'], user['user'], user['count']))
                            user['count'] = 0
                            print(f'Insert {user["user"]} success')

        except Exception as ex:
            print(f"[INFO] - {ex}")
        finally:
            if connection:
                print('Connection close')
                connection.close()


async def display_fword():
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
            cursor.execute('SELECT * FROM fwords;')
            users = cursor.fetchall()
            sort_users = sorted(users, key=lambda x: x[3], reverse=True)
            for i in range(len(users)):
                await dp.bot.send_message(text=f"{i + 1} место: {sort_users[i][2]} - {sort_users[i][3]} нецензурных слов", chat_id=495432329)

    except Exception as ex:
        print(f"[INFO] - {ex}")
    finally:
        if connection:
            print('Connection close')
            connection.close()


