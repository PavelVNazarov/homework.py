# Домашнее задание по теме "Логирование"
# Назаров ПВ
# tests_12_4.py

import logging
import unittest
from rt_with_exceptions import Runner

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s')


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner('Вося', -5) 
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            runner = Runner(123, 10)
            runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")


if __name__ == '__main__':
    unittest.main()
