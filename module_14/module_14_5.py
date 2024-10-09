# Домашнее задание по теме "Написание примитивной ORM"
# Назаров ПВ
# module_14_5.py

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import State, StatesGroup
from aiogram.utils import executor
from crud_functions import initiate_db, add_user, is_included, get_all_products

API_TOKEN = 'YOUR_API_TOKEN'

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Добро пожаловать!")

@dp.message_handler(lambda message: message.text == "Регистрация")
async def sing_up(message: types.Message):
    await message.reply("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text
    if not is_included(username):
        await state.update_data(username=username)
        await message.reply("Введите свой email:")
        await RegistrationState.email.set()
    else:
        await message.reply("Пользователь существует, введите другое имя:")
        await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.reply("Введите свой возраст:")
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    age = message.text
    data = await state.get_data()
    username = data.get("username")
    email = data.get("email")

    add_user(username, email, age)
    await message.reply("Вы успешно зарегистрированы!")
    await state.finish()

if __name__ == '__main__':
    initiate_db()
    populate_initial_products()  # Чтобы добавить начальные продукты
    executor.start_polling(dp, skip_updates=True)
Объяснение
Функции базы данных: Мы создали функции для инициализации базы данных и выполнения CRUD операций.
Страны регистрации: Определены состояния для ввода данных пользователя.
Обработчики сообщений: Реализованы функции, чтобы передавать данные через состояния.
