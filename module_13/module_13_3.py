# Домашнее задание по теме "Методы отправки сообщений".
# Назаров ПВ
# module_13_3.py

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram import MemoryStorage
from aiogram import executor

# UrUnNazBot чатбот в Телеграм
API_TOKEN = 'YOUR_API_TOKEN'  # Заменить 'YOUR_API_TOKEN' на токен бота

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    response_text = 'Привет! Я бот, помогающий твоему здоровью.'
    await message.reply(response_text)

@dp.message_handler(lambda message: True)
async def all_messages(message: types.Message):
    response_text = 'Введите команду /start, чтобы начать общение.'
    await message.reply(response_text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
