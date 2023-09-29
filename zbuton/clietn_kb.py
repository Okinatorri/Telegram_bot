from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

b1 = KeyboardButton('Інформація та допомога 🙌')
#b2 = KeyboardButton('/start')
b3 = KeyboardButton("Меню ☕️")
#b4 = KeyboardButton('Поделиться номером', request_contact=True)
#b5 = KeyboardButton('Отправить где я', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b3, b1)
