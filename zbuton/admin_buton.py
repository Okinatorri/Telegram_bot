from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


buton_load = KeyboardButton('/Загрузить')
buton_delete = KeyboardButton('/Удалить')

buton_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(buton_load).add(buton_delete)
