# Домашнее задание по теме "Создание исключений".".
# Назаров ПВ
# module_8_3.py

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model, vin, numbers):
        self.__is_valid_vin(vin)
        self.__vin = vin
        self.__is_valid_numbers(numbers)
        self.__numbers = numbers
        self.model = model

    @staticmethod
    def __is_valid_vin(vin_number):
        if isinstance(vin_number, int):
            if 1000000 <= vin_number <= 9999999:
                return True
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        raise IncorrectVinNumber('Некорректный тип vin номер')

    @staticmethod
    def __is_valid_numbers(numbers):
        if isinstance(numbers, str):
            if len(numbers) == 6:
                return True
            raise IncorrectVinNumber('Неверная длина номера')
        raise IncorrectVinNumber('Некорректный тип данных для номеров')


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
