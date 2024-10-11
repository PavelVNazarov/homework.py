# Домашнее задание по теме "Инлайн клавиатуры".
# Назаров ПВ
# module_13_6.py

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage

#API_TOKEN = 'YOUR_API_TOKEN'  # Заменить 'YOUR_API_TOKEN' на токен бота

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    sex = State()

# Создание клавиатуры
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
keyboard.add(button_calculate, button_info)

# Создание inline-клавиатуры
inline_keyboard = InlineKeyboardMarkup()
button_calories = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_keyboard.add(button_calories, button_formulas)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    response_text = 'Привет! Я бот, помогающий твоему здоровью.'
    await message.reply(response_text, reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def main_menu(message: types.Message):
    await message.reply('Выберите опцию:', reply_markup=inline_keyboard)

@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    formula_info = ("Формула Миффлина - Сан Жеора:\n"
                    "Для женщин: 10 * вес + 6.25 * рост - 5 * возраст - 161\n"
                    "Для мужчин: 10 * вес + 6.25 * рост - 5 * возраст + 5")
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, formula_info)

@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_sex(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, 'Введите свой пол (м/ж):')
    await UserState.sex.set()  # Устанавливаем состояние для пола

@dp.message_handler(state=UserState.sex)
async def set_age(message: types.Message, state: FSMContext):
    await state.update_data(sex=message.text.lower())  # Сохраняем пол
    await message.reply('Введите свой возраст:')
    await UserState.age.set()  # Переход к следующему состоянию

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
    sex = data.get('sex')  # Получаем пол

    # Формула Миффлина - Сан Жеора
    if sex == 'ж':
        calories = 10 * weight + 6.25 * growth - 5 * age - 161  # для женщин
    else:
        calories = 10 * weight + 6.25 * growth - 5 * age + 5  # для мужчин

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
