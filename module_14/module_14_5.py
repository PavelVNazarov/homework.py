# Домашнее задание по теме "Написание примитивной ORM"
# Назаров ПВ
# module_14_5.py

from aiogram import Bot, Dispatcher, types
from aiogram import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import aiohttp
from crud_functions import initiate_db, get_all_products, add_user, is_included

API_TOKEN = 'YOUR_API_TOKEN'  # Замените на Ваш токен
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    sex = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()

# Инициализация базы данных
initiate_db()

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
button_buy = KeyboardButton('Купить')
button_register = KeyboardButton('Регистрация')  # Кнопка регистрации
keyboard.add(button_calculate, button_info, button_buy, button_register)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    response_text = 'Привет! Я бот, помогающий твоему здоровью.'
    await message.reply(response_text, reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == 'Регистрация')
async def sing_up(message: types.Message):
    await RegistrationState.username.set()  # Устанавливаем состояние для username
    await message.reply("Введите имя пользователя (только латинский алфавит):")

@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text
    if is_included(username):
        await message.reply("Пользователь существует, введите другое имя.")
    else:
        await state.update_data(username=username)
        await RegistrationState.next()  # Переход к следующему состоянию
        await message.reply("Введите свой email:")

@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await RegistrationState.next()  # Переход к следующему состоянию
    await message.reply("Введите свой возраст:")

@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    age = message.text
    user_data = await state.get_data()
    username = user_data.get("username")
    email = user_data.get("email")

    add_user(username, email, age)  # Добавляем пользователя в БД
    await message.reply("Вы успешно зарегистрированы!")
    await state.finish()  # Завершаем состояние
