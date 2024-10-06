# Домашнее задание по теме "Систематизация и пропуск тестов".
# Назаров ПВ
# suite_12_3.py

import unittest
from tests_12_3 import TournamentTest, RunnerTest

# Создаем объект TestSuite и добавляем туда тесты
test_suite = unittest.TestSuite()
test_suite.addTests(unittest.loader.TestLoader().loadTestsFromTestCase(RunnerTest))
test_suite.addTests(unittest.loader.TestLoader().loadTestsFromTestCase(TournamentTest))

# Создание TextTestRunner с verbosity=2
runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_suite)
