# Домашнее задание по теме "Клавиатура кнопок".
# Назаров ПВ
# module_13_5.py

from aiogram import Bot, Dispatcher, types
#from aiogram import MemoryStorage
from aiogram import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = 'YOUR_API_TOKEN'  # Заменить 'YOUR_API_TOKEN' на токен бота

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Создание клавиатуры
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
keyboard.add(button_calculate, button_info)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    response_text = 'Привет! Я бот, помогающий твоему здоровью.'
    await message.reply(response_text, reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def set_age(message: types.Message):
    await message.reply('Введите свой возраст:')
    await UserState.age.set()  # Устанавливаем состояние

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)  # Сохраняем возраст
    await message.reply('Введите свой рост (в см):')
    await UserState.growth.set()  # Переход к следующему состоянию

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)  # Сохраняем рост
    await message.reply('Введите свой вес (в кг):')
    await UserState.weight.set()  # Переход к следующему состоянию

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)  # Сохраняем вес

    data = await state.get_data()  # Получаем все сохраненные данные
    age = int(data.get('age'))
    growth = int(data.get('growth'))
    weight = int(data.get('weight'))

    # Формула Миффлина - Сан Жеора для женщин
    calories = 10 * weight + 6.25 * growth - 5 * age - 161  # Можно адаптировать для мужчин

    await message.reply(f'Ваша норма калорий: {calories:.2f} ккал')
    await state.finish()  # Завершаем состояние

@dp.message_handler(lambda message: message.text == 'Информация')
async def info(message: types.Message):
    await message.reply('Информация о боте: Я предназначен для расчета калорий и улучшения Вашего здоровья.')

@dp.message_handler(lambda message: True)
async def all_messages(message: types.Message):
    await message.reply('Введите команду /start или нажмите на кнопку, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
