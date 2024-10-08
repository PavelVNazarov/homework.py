# Домашнее задание по теме "Систематизация и пропуск тестов".
# Назаров ПВ
# tests_12_3.py

from runner import Runner, Tournament
import unittest
from functools import wraps

def skip_if_frozen(test_case):
    @wraps(test_case)
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        return test_case(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False  # Меняем на True, чтобы заморозить тесты

    @skip_if_frozen
    def test_walk(self):
        walker = Runner('Turtle')
        for _ in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50,
                         f"Дистанции не равны {walker.distance} != 50")

    @skip_if_frozen
    def test_run(self):
        runner = Runner('Rabbit')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100,
                         f"Дистанции не равны {runner.distance} != 100")

    @skip_if_frozen
    def test_challenge(self):
        runner = Runner('Rabbit')
        walker = Runner('Turtle')

        for _ in range(10):
            runner.run()

        for _ in range(10):
            walker.walk()

        self.assertNotEqual(runner.distance, walker.distance,
                            f"Дистанции равны {runner.distance} == {walker.distance}")

class TournamentTest(unittest.TestCase):
    is_frozen = True  # Меняйте на False, чтобы выполнить тесты

    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", speed=10)
        self.runner2 = Runner("Андрей", speed=9)
        self.runner3 = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    @skip_if_frozen
    def test_race_usain_and_nik(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        for num, result in results.items():
            results[num] = result.name
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    @skip_if_frozen
    def test_race_andrey_and_nik(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        for num, result in results.items():
            results[num] = result.name
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    @skip_if_frozen
    def test_race_usain_andrey_and_nik(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        for num, result in results.items():
            results[num] = result.name
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

if __name__ == '__main__':
    unittest.main()
