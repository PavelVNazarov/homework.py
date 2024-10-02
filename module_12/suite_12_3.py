# Домашнее задание по теме "Систематизация и пропуск тестов".
# Назаров ПВ
# module_12_3.py
import unittest

import tests_12_3
# Декоратор для пропуска тестов
def skip_if_frozen(func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            self.skipTest("Тесты в этом кейсе заморожены")
        return func(self, *args, **kwargs)
    return wrapper

# Модификация тестов
class RunnerTest(unittest.TestCase):
    is_frozen = False  # Измените это значение на True для пропуска всех тестов

    @skip_if_frozen
    def test_challenge(self):
        # Ваш тест
        pass

    @skip_if_frozen
    def test_run(self):
        # Ваш тест
        pass

    @skip_if_frozen
    def test_walk(self):
        # Ваш тест
        pass

class TournamentTest(unittest.TestCase):
    is_frozen = True  # Измените это значение на False для выполнения всех тестов

    @skip_if_frozen
    def test_first_tournament(self):
        # Ваш тест
        pass

    @skip_if_frozen
    def test_second_tournament(self):
        # Ваш тест
        pass

    @skip_if_frozen
    def test_third_tournament(self):
        # Ваш тест
        pass

if __name__ == '__main__':
    suite = unittest.TestSuite()
    # Добавляем тесты в тестовый набор
    suite.addTest(unittest.makeSuite(RunnerTest))
    suite.addTest(unittest.makeSuite(TournamentTest))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
