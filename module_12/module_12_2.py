# Домашнее задание по теме "Простые Юнит-Тесты"
# Назаров ПВ
# module_12_2.py

import unittest
from runner import Runner, Tournament

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        # Создаём объекты бегунов
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        new_result = {}
        for name, result in cls.all_results.items():
            new_result[name] = result.name
            print(new_result)

    def test_race_usain_vs_nik(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        last_runner = self.all_results[max(self.all_results.keys())]
        self.assertTrue(last_runner.name != "Усэйн", f"Последний бегущий: {last_runner.name} не равен ожидаемому 'Усэйн'")

    def test_race_andrey_vs_nik(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        last_runner = self.all_results[max(self.all_results.keys())]
        self.assertTrue(last_runner.name != "Андрей", f"Последний бегущий: {last_runner.name} не равен ожидаемому 'Андрей'")

    def test_race_usain_vs_andrey_vs_nik(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        last_runner = self.all_results[max(self.all_results.keys())]
        self.assertTrue(last_runner.name != "Усэйн", f"Последний бегущий: {last_runner.name} не равен ожидаемому 'Усэйн'")

if __name__ == '__main__':
    unittest.main()
