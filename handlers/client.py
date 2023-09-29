#Клиенская часть бота!
from aiogram import types, Dispatcher
from create_bot import dp, bot
from zbuton import kb_client
from aiogram.types import ReplyKeyboardRemove, Message
from data_base import sqlite_db
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text



#@dp.message_handler(commands=['start'])
async def commands_start(message: types.Message):
   # try:
    await bot.send_message(message.from_user.id, 'Стартуем!!!', reply_markup=kb_client)
    await message.delete()

#@dp.message_handler(commands=['Расположение'])
async def Angel_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Мы находимся в г. Киверцы ул. Парковая 25. У нас самые низкие цены только для вас. Вы можете поддержать нас купив у нас что нибуть.')


@dp.callback_query_handler(lambda c: c.data.startswith('buy_'))
async def process_buy_callback(callback_query: types.CallbackQuery):
    item_id = callback_query.data[4:]  # Получаем ID товара из callback_data
    await sqlite_db.buy_item(callback_query.message.chat.id, item_id)
    await bot.answer_callback_query(callback_query.id, text="Товар добавлен в корзину!", show_alert=True)


async def Angel_menu_command(message: types.Message):
    items = sqlite_db.get_menu_items()

    for item in items:
        # Отправляем сообщение с фотографией, названием, описанием и кнопкой "Купить"
        await message.answer_photo(
            item[0],  # Путь к фото (в вашем случае item[0] это путь к фото)
            caption=f"{item[1]}\nОписание: {item[2]}\nЦена: {item[3]}",  # Название, описание и цена товара
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton(text="Купить", callback_data=f'buy_{item[1]}')]  # Кнопка "Купить"
                ]
            )
        )



def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start'])
    dp.register_message_handler(Angel_place_command, lambda message: message.text and 'Інформація та допомога 🙌' in message.text)
    dp.register_message_handler(Angel_menu_command, lambda message: message.text and 'Меню ☕️' in message.text)
    #dp.register_message_handler(process_buy_callback, lambda c: c.data.startswith('buy_'))
