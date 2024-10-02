# Домашнее задание по теме "Простые Юнит-Тесты"
# Назаров ПВ
# module_12_2_2.py

import unittest
from runner import Runner, Tournament

class TournamentTest(unittest.TestCase):
    all_results = []

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        # Создаём объекты бегунов
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for dict in cls.all_results:
             print(dict)

    def test_race_usain_vs_nik(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        for name, result in results.items():
            results[name] = result.name
        self.all_results.append(results)
        last_runner = results[max(list(results))]
        self.assertTrue(last_runner != "Усэйн", f"Последний бегущий: {last_runner} не равен ожидаемому 'Усэйн'")

    def test_race_andrey_vs_nik(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()

        for name, result in results.items():
            results [name] = result.name
        self.all_results.append(results)
        #last_runner = self.all_results[max(list(self.all_results))]
        #self.assertTrue(last_runner != "Андрей", f"Последний бегущий: {last_runner} не равен ожидаемому 'Андрей'")

    def test_race_usain_vs_andrey_vs_nik(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        for name, result in results.items():
            results[name] = result.name
        self.all_results.append(results)
        #last_runner = self.all_results[max(list(self.all_results))]
        #self.assertTrue(last_runner != "Усэйн", f"Последний бегущий: {last_runner} не равен ожидаемому 'Усэйн'")



if __name__ == '__main__':
    unittest.main()
