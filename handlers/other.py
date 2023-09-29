#Общяя часть бота!
from aiogram import types, Dispatcher
from create_bot import dp, bot
import json, string

#@dp.message_handler()
async def echo_send(message: types.Message):
        # await message.answer(message.text)
        # await message.reply(message.text)
    if message.text == "Привет":
        await bot.send_message(message.from_user.id, "Добрый день!")

def register_handler_other(dp : Dispatcher):
    dp.register_message_handler(echo_send)
