# Домашнее задание по теме "Систематизация и пропуск тестов".
# Назаров ПВ
# tests_12_3.py

from runner import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):

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

    def test_race_usain_and_nik(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        for num, result in results.items():
            results[num] = result.name
        self.all_results[len(self.all_results) + 1] = results

        # Проверяем, что Ник всегда последний
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_race_andrey_and_nik(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        for num, result in results.items():
            results[num] = result.name
        self.all_results[len(self.all_results) + 1] = results

        # Проверяем, что Ник всегда последний
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_race_usain_andrey_and_nik(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        for num, result in results.items():
            results[num] = result.name
        self.all_results[len(self.all_results) + 1] = results

        # Проверяем, что Ник всегда последний
        self.assertTrue(results[max(results.keys())] == "Ник")


if __name__ == '__main__':
    unittest.main()
