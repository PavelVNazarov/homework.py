# Домашнее задание по теме "Машина состояний".
# Назаров ПВ
# module_13_4.py

mport asyncio
from aiogram import Bot, Dispatcher, types
from aiogram import MemoryStorage
from aiogram import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StateGroup

# UrUnNazBot чатбот в Телеграм
API_TOKEN = 'YOUR_API_TOKEN'  # Заменить 'YOUR_API_TOKEN' на токен твоего бота

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StateGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    response_text = 'Привет! Я бот, помогающий твоему здоровью.'
    await message.reply(response_text)

@dp.message_handler(commands=['calories'])
async def set_age(message: types.Message):
    await message.reply('Введите свой возраст:')
    await UserState.age.set() 

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)  
    await message.reply('Введите свой рост (в см):')
    await UserState.growth.set()  

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text) 
    await message.reply('Введите свой вес (в кг):')
    await UserState.weight.set() 

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text) 

    data = await state.get_data()  
    age = int(data.get('age'))
    growth = int(data.get('growth'))
    weight = int(data.get('weight'))

    # Формула Миффлина - Сан Жеора для женщин
    calories = 10 * weight + 6.25 * growth - 5 * age + 161  

    await message.reply(f'Ваша норма калорий: {calories:.2f} ккал')
    await state.finish()  

@dp.message_handler(lambda message: True)
async def all_messages(message: types.Message):
    await message.reply('Введите команду /start или /calories, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
