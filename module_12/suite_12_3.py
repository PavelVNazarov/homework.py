# Домашнее задание по теме "Систематизация и пропуск тестов".
# Назаров ПВ
# suite_12_3.py

import unittest
from tests_12_3 import RunnerTest, TournamentTest

# Создание тестового набора
suite = unittest.TestSuite()
loader = unittest.TestLoader()

# Добавляем тесты
suite.addTests(loader.loadTestsFromTestCase(RunnerTest))
suite.addTests(loader.loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
