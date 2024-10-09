# Домашнее задание по теме "Доработка бота"
# Назаров ПВ
# module_14_3.py

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram import MemoryStorage
from aiogram import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StateGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = 'YOUR_API_TOKEN'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StateGroup):
    age = State()
    growth = State()
    weight = State()

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
button_buy = KeyboardButton('Купить')  # Новая кнопка
keyboard.add(button_calculate, button_info, button_buy)  # Добавляем кнопку "Купить"

inline_keyboard = InlineKeyboardMarkup()
button_calories = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
inline_keyboard.add(button_calories, button_formulas)

# Новое инлайн меню для покупок
product_keyboard = InlineKeyboardMarkup()
product_buttons = [
    InlineKeyboardButton('Product1', callback_data='product_buying'),
    InlineKeyboardButton('Product2', callback_data='product_buying'),
    InlineKeyboardButton('Product3', callback_data='product_buying'),
    InlineKeyboardButton('Product4', callback_data='product_buying')
]
product_keyboard.add(*product_buttons)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    response_text = 'Привет! Я бот, помогающий твоему здоровью.'
    await message.reply(response_text, reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def main_menu(message: types.Message):
    await message.reply('Выберите опцию:', reply_markup=inline_keyboard)

@dp.message_handler(lambda message: message.text == 'Купить')
async def get_buying_list(message: types.Message):
    # Выводим информацию о товаре
    products = [
        {"name": "Product1", "description": "Описание 1", "price": 100},
        {"name": "Product2", "description": "Описание 2", "price": 200},
        {"name": "Product3", "description": "Описание 3", "price": 300},
        {"name": "Product4", "description": "Описание 4", "price": 400},
    ]

    for product in products:
        product_info = f'Название: {product["name"]} | Описание: {product["description"]} | Цена: {product["price"]}₽'
        await message.reply(product_info)
        # Здесь можно отправить картинку, используя await bot.send_photo() и передавая photo_url
        # await bot.send_photo(message.chat.id, photo_url)  # Замените photo_url на действительный URL картинки.

    await message.reply('Выберите продукт:', reply_markup=product_keyboard)

@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery):
    await call.message.reply('Введите свой возраст:')
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
    calories = 10 * weight + 6.25 * growth - 5 * age + 161
    await message.reply(f'Ваша норма калорий: {calories:.2f} ккал')
    await state.finish() 

@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    message = "Формула Миффлина-Сан Жеора:\n\n" \
              "Для женщин: 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) + 161\n" \
              "Для мужчин: 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) + 5"
    await call.message.reply(message)

@dp.message_handler(lambda message: message.text == 'Информация')
async def info(message: types.Message):
    await message.reply('Информация о боте: Я предназначен для расчета калорий и улучшения Вашего здоровья.')

@dp.message_handler(lambda message: True)
async def all_messages(message: types.Message):
    await message.reply('Введите команду /start или нажмите на кнопку, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
Объяснение внесённых изменений:
Добавлена кнопка "Купить": Теперь она присутствует в обычной клавиатуре меню.
Создано инлайн-меню для выбора продуктов: Теперь при нажатии на кнопку "Купить" выводится информация о каждом продукте.
Добавлены функции обработки выбора продуктов: В функции get_buying_list выводятся наименование, описание и цена для каждого продукта.
Не забудь заменить YOUR_API_TOKEN на действительный токен твоего бота. Если потребуется добавить картинки, тебе понадобится URL картинок или локальные файлы с изображениями.

#######
# другая версия, полнее
#####################

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram import MemoryStorage
from aiogram import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StateGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = 'YOUR_API_TOKEN'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StateGroup):
    age = State()
    growth = State()
    weight = State()

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
button_buy = KeyboardButton('Купить')  # Добавленная кнопка "Купить"
keyboard.add(button_calculate, button_info, button_buy)

inline_keyboard = InlineKeyboardMarkup()
button_calories = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
inline_keyboard.add(button_calories, button_formulas)

# Добавление inline-кнопок для продуктов
product_inline_keyboard = InlineKeyboardMarkup()
for i in range(1, 5):  # Создаем 4 кнопки продукта
    button_product = InlineKeyboardButton(f'Product{i}', callback_data='product_buying')
    product_inline_keyboard.add(button_product)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    response_text = 'Привет! Я бот, помогающий твоему здоровью.'
    await message.reply(response_text, reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def main_menu(message: types.Message):
    await message.reply('Выберите опцию:', reply_markup=inline_keyboard)

@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery):
    await call.message.reply('Введите свой возраст:')
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
    calories = 10 * weight + 6.25 * growth - 5 * age + 161
    await message.reply(f'Ваша норма калорий: {calories:.2f} ккал')
    await state.finish() 

@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    message = "Формула Миффлина-Сан Жеора:\n\n" \
              "Для женщин: 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) + 161\n" \
              "Для мужчин: 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) + 5"
    await call.message.reply(message)

@dp.message_handler(lambda message: message.text == 'Информация')
async def info(message: types.Message):
    await message.reply('Информация о боте: Я предназначен для расчета калорий и улучшения Вашего здоровья.')

@dp.message_handler(lambda message: message.text == 'Купить')
async def get_buying_list(message: types.Message):
    for i in range(1, 5):
        product_info = f'Название: Product{i} | Описание: описание {i} | Цена: {i * 100}'
        await message.reply(product_info)
        # Здесь Вы можете вставить код для отправки изображения продуктов, если они у Вас есть. 
        # Например:
        # await bot.send_photo(message.chat.id, photo='URL_или_файл_с_изображением')
    
    await message.reply('Выберите продукт для покупки:', reply_markup=product_inline_keyboard)

@dp.callback_query_handler(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.reply("Вы успешно приобрели продукт!")

@dp.message_handler(lambda message: True)
async def all_messages(message: types.Message):
    await message.reply('Введите команду /start или нажмите на кнопку, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
Что добавлено:
Кнопка "Купить" в основном меню.
Inline меню с кнопками для выбора продуктов.
Хэндлеры для обработки покупки и вывода информации о продуктах.
Функция, выводящая информацию о каждом продукте и позволяющая пользователю выбрать продукт для покупки.
