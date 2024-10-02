# Домашнее задание по теме "Логирование"
# Назаров ПВ
# tests_12_4.py

import unittest
import runner
import logging
import unittest
from runner import Runner  # assuming the Runner class is in a separate module

logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s: %(message)s',
                    filename='runner_tests.log',
                    filemode='w',
                    encoding='UTF-8')


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner('Ahil',speed=-5)  # passing a negative speed value
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            runner = Runner(name=123)  # passing a non-string value for name
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner")
