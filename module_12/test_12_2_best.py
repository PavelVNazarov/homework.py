# Домашнее задание по теме "Методы Юнит-тестирования"
# Назаров ПВ
# test_12_2_best.py

from runner_and_tournament import Runner, Tournament
import unittest
import itertools

class TournamentTest(unittest.TestCase):

    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runners = [Runner("Усэйн", speed=10),
            Runner("Андрей", speed=9),
            Runner("Ник", speed=3),]

        self.runners_group = ((self.runners[0], self.runners[1]),
                             (self.runners[0], self.runners[2]),
                             (self.runners[1], self.runners[2]),
                             (self.runners[1], self.runners[0]),
                             (self.runners[2], self.runners[1]),
                             (self.runners[2], self.runners[0]),
                             (self.runners[0], self.runners[1], self.runners[2]),
                             (self.runners[1], self.runners[2], self.runners[0]),
                             (self.runners[2], self.runners[0], self.runners[1]),
                             (self.runners[0], self.runners[2], self.runners[1]),
                             (self.runners[1], self.runners[0], self.runners[2]),
                             (self.runners[2], self.runners[1], self.runners[0]),)


    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_all_races(self):
        for distance in range(10, 130, 10):
            for runners_combination in self.runners_group:
                tournament = Tournament(distance, *runners_combination)
                results = tournament.start()
            
                # Создаем словарь с номером места в качестве ключа и именем бегуна в качестве значения
                results_dict = {place: runner.name for place, runner in results.items()}
            
                sorted_results = sorted(runners_combination, key=lambda x: x.speed, reverse=True)
                result_names = [runner.name for runner in sorted_results]
            
                fastest_runner = result_names[0]
                slowest_runner = result_names[-1]
            
                print(f"Дистанция: {distance}м, Участники: {[runner.name for runner in runners_combination]}")
                print(f'Результаты: {results_dict}')  # Отображаем имена бегунов
            
                try:
                    self.assertTrue(fastest_runner == results_dict[1],
                                    f"Ошибка: {fastest_runner} не на первом месте на {distance}м")
                except AssertionError as e:
                    print(f"Тест не прошел: {e}")
            
                try:
                    self.assertTrue(slowest_runner == results_dict[len(sorted_results)],
                                    f"Ошибка: {slowest_runner} не на последнем месте на {distance}м")
                except AssertionError as e:
                    print(f"Тест не прошел: {e}")

if __name__ == '__main__':
    unittest.main()
