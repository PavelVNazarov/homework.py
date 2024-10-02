# Домашнее задание по теме "Систематизация и пропуск тестов".
# Назаров ПВ
# module_12_3.py

import unittest

# Модуль runner должен быть импортирован
from runner import Runner, Tournament


def frozen_test_decorator(is_frozen):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if is_frozen:
                print("Тесты в этом кейсе заморожены")
                # Пропускаем тест с помощью unittest.SkipTest
                raise unittest.SkipTest("Тесты в этом кейсе заморожены")
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @frozen_test_decorator(is_frozen)
    def test_run(self):
        runner = Runner("TestRunner")
        runner.run()
        self.assertEqual(runner.distance, 10)

    @frozen_test_decorator(is_frozen)
    def test_walk(self):
        runner = Runner("TestRunner")
        runner.walk()
        self.assertEqual(runner.distance, 5)

    @frozen_test_decorator(is_frozen)
    def test_challenge(self):
        runner1 = Runner("Runner1", 6)
        runner2 = Runner("Runner2", 4)
        runner1.run()
        runner2.run()
        self.assertTrue(runner1.distance > runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @frozen_test_decorator(is_frozen)
    def test_first_tournament(self):
        runner1 = Runner("Runner1", 6)
        runner2 = Runner("Runner2", 4)
        tournament = Tournament(20, runner1, runner2)
        finishers = tournament.start()
        self.assertIn(1, finishers)

    @frozen_test_decorator(is_frozen)
    def test_second_tournament(self):
        runner1 = Runner("Runner3", 5)
        runner2 = Runner("Runner4", 7)
        tournament = Tournament(30, runner1, runner2)
        finishers = tournament.start()
        self.assertIn(1, finishers)

    @frozen_test_decorator(is_frozen)
    def test_third_tournament(self):
        runner1 = Runner("Runner5", 8)
        runner2 = Runner("Runner6", 6)
        tournament = Tournament(40, runner1, runner2)
        finishers = tournament.start()
        self.assertIn(1, finishers)


# Создание объекта TestSuite и его выполнение
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RunnerTest))
    suite.addTest(unittest.makeSuite(TournamentTest))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

#Декоратор frozen_test_decorator: Он принимает параметр is_frozen. Если is_frozen равно True, тест пропускается и выводится сообщение.

#Классы RunnerTest и TournamentTest: В каждом классе добавлен атрибут is_frozen. Методы тестов используют декоратор для проверки этого флага.

#Suite: Создается TestSuite, который добавляет тесты из обоих классов, и затем используется TextTestRunner для их запуска.
