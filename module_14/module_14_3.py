# Домашнее задание по теме "Доработка бота"
# Назаров ПВ
# module_14_3.py

from aiogram import Bot, Dispatcher, types
from aiogram import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import aiohttp

API_TOKEN = 'YOUR_API_TOKEN'  # Заменить 'YOUR_API_TOKEN' на токен бота

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    sex = State()

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
button_buy = KeyboardButton('Купить')  # Новая кнопка
keyboard.add(button_calculate, button_info, button_buy)  # Добавляем кнопку в клавиатуру

inline_keyboard = InlineKeyboardMarkup()
button_calories = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_keyboard.add(button_calories, button_formulas)

products_info = [
    ["California Gold Nutrition Baby Vitamin D3 Liquid","Вариант для самых маленьких. Также в составе есть ДГК (докозагексаеновая кислота) — омега-3 жирная кислота, необходимая для формирования мозга, нервной системы и зрения у ребенка.","100","https://ltdfoto.ru/images/2024/10/17/babyd34c24ca37eabfb2b4.png","BabyD3"],
    ["California Gold Nutrition Omega-3 Premium Fish Oil","Капсулы с рыбьим жиром омега-3 премиального качества. Они содержат ключевые омега-3 жирные кислоты, такие как ДГК и ЭПК.","100","https://ltdfoto.ru/images/2024/10/17/omega324684226cd955fae.png","Omega-3"],
    ["Магний хелат Эвалар","Биологически активная добавка в таблетках. Этот магний в хелатной форме также хорошо усваивается организмом.","100","https://ltdfoto.ru/images/2024/10/17/magnibed42d251ce0a26b.png","Magni"],
    ["GLS Коллаген 1000","Биологически активная добавка (БАД) к пище с гидролизатом рыбного коллагена.","100","https://ltdfoto.ru/images/2024/10/17/collagen5263a67645df4975.png","Collagen"],]

# Новое Inline меню для покупки
product_inline_keyboard = InlineKeyboardMarkup()
for product in products_info:  # Создаем 4 кнопки продукта
    button_product = InlineKeyboardButton(product[4], callback_data='product_buying')
    product_inline_keyboard.add(button_product)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    response_text = 'Привет! Я бот, помогающий твоему здоровью.'
    await message.reply(response_text, reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def main_menu(message: types.Message):
    await message.reply('Выберите опцию:', reply_markup=inline_keyboard)

@dp.message_handler(lambda message: message.text == 'Купить')  # Новый хэндлер
async def get_buying_list(message: types.Message):
    for product in products_info:
        #await message.reply(product[0])  # Отправляем информацию
        await message.reply(f'Название: {product[0]} | Описание: {product[1]} | Цена: {product[2]}')
        # Загружаем изображение из URL
        async with aiohttp.ClientSession() as session:
            async with session.get(product[3]) as resp:
                if resp.status == 200:
                    photo = await resp.read()
                    await bot.send_photo(message.chat.id, photo=photo)

    await message.reply('Выберите продукт для покупки:', reply_markup=product_inline_keyboard)

@dp.callback_query_handler(lambda call: call.data.startswith('product_buying'))
async def send_confirm_message(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "Вы успешно приобрели продукт!")

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

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    try:
        age = int(message.text)
        if age < 0 or age > 120:  # пример проверки валидности возраста
            raise ValueError
        await state.update_data(age=age)
        await message.reply('Введите свой рост (в см):')
        await UserState.growth.set()
    except ValueError:
        await message.reply('Пожалуйста, введите корректный возраст!')


@dp.message_handler(state=UserState.sex)
async def set_age(message: types.Message, state: FSMContext):
    if message.text.lower() not in ['м', 'ж']:
        await message.reply('Пожалуйста, введите "м" для мужчин или "ж" для женщин.')
        return
    await state.update_data(sex=message.text.lower())
    await message.reply('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    try:
        growth = int(message.text)
        if growth <= 0:  # проверка на положительность роста
            raise ValueError
        await state.update_data(growth=growth)
        await message.reply('Введите свой вес (в кг):')
        await UserState.weight.set()
    except ValueError:
        await message.reply('Пожалуйста, введите корректный рост в сантиметрах!')

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    try:
        weight = int(message.text)
        if weight <= 0:  # проверка на положительность веса
            raise ValueError
        await state.update_data(weight=weight)
        data = await state.get_data()
        age = data.get('age')
        growth = data.get('growth')
        weight = data.get('weight')
        sex = data.get('sex')

        if sex == 'ж':
            calories = 10 * weight + 6.25 * growth - 5 * age - 161
        else:
            calories = 10 * weight + 6.25 * growth - 5 * age + 5
        await message.reply(f'Ваша норма калорий: {calories:.2f} ккал')
        await state.finish()  # Завершаем состояние
    except ValueError:
        await message.reply('Пожалуйста, введите корректный вес в килограммах!')

@dp.message_handler(lambda message: message.text == 'Информация')
async def info(message: types.Message):
    await message.reply('Информация о боте: Я предназначен для расчета калорий и улучшения Вашего здоровья.')

@dp.message_handler(lambda message: True)
async def all_messages(message: types.Message):
    await message.reply('Введите команду /start или нажмите на кнопку, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
