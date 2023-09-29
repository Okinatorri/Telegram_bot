import sqlite3 as sq
from create_bot import bot
import os

# Получаем абсолютный путь к текущей директории
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Собираем путь к базе данных
DATABASE_PATH = os.path.join(CURRENT_DIR, '..', 'Angel_Cafe.db')



def sql_start():
    global base, cur
    base = sq.connect('Angel_Cafe.db')
    cur = base.cursor()
    if base:
        print('Data base conected ok')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS cart(user_id INTEGER, item_id INTEGER)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')

async def sql_read2():
    return cur.execute('SELECT * FROM menu'). fetchall()

async def sql_delete_command(data):
    cur.execute('DELETE FROM menu WHERE name == ?', (data,))
    base.commit()

def get_menu_items():
    connection = sq.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM menu')
    items = cursor.fetchall()
    connection.close()
    return items

async def buy_item(user_id, item_id):
    connection = sq.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute('INSERT INTO cart (user_id, item_id) VALUES (?, ?)', (user_id, item_id))
    connection.commit()
    connection.close()








