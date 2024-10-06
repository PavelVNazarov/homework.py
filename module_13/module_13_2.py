# Домашнее задание по теме "Хендлеры обработки сообщений".
# Назаров ПВ
# module_13_2.py

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram import MemoryStorage
from aiogram import executor

# UrUnNazBot чатбот в Телеграм
API_TOKEN = 'YOUR_API_TOKEN'  # Замени 'YOUR_API_TOKEN' на токен твоего бота

bot = Bot(token=API_TOKEN)
#storage = MemoryStorage()
#dp = Dispatcher(bot, storage=storage)
dp = Dispatcher(bot, storage = MemoryStorage())
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.reply('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler(lambda message: True)
async def all_messages(message: types.Message):
    print('Введите команду /start, чтобы начать общение.')
    await message.reply('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
