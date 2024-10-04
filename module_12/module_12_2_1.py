# Домашнее задание по теме "Простые Юнит-Тесты"
# Назаров ПВ
# module_12_2.py - решение подогнано под ответ
# module_12_2_2.py лучше

import unittest
from runner import Runner, Tournament

class  TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for key in cls.all_results:
            new_result = {}
            for name, result in cls.all_results[key].items():
                new_result[name] = result.name
            print(new_result)

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    def test_race_usain_vs_nik(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results[1] = results
        last_runner = results[max(list(results))]
        self.assertTrue(last_runner, "Усэйн")# f"Последний бегущий: {last_runner} не равен ожидаемому 'Усэйн'")

    def test_race_andrey_vs_nik(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[2] = results
        last_runner = results[max(list(results))]
        self.assertTrue(last_runner, "Андрей")# f"Последний бегущий: {last_runner} не равен ожидаемому 'Андрей'")

    def test_race_usain_vs_andrey_vs_nik(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[3] = results
        last_runner = results[max(list(results))]
        self.assertTrue(last_runner, "Усэйн")  #, f"Последний бегущий: {last_runner} не равен ожидаемому 'Усэйн'")

if __name__ == '__main__':
    unittest.main()
