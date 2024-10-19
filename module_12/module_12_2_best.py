
from runner_and_tournament import Runner, Tournament
import unittest
import itertools

class TournamentTest(unittest.TestCase):

    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runners = [
            Runner("Усэйн", speed=10),
            Runner("Андрей", speed=9),
            Runner("Ник", speed=3),
        ]

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_all_races(self):
        distances = [50, 100, 150]  # Определите возможные дистанции
        for distance in distances:
            for group in range(2, len(self.runners) + 1):
                for runners_combination in itertools.combinations(self.runners, group):
                    tournament = Tournament(distance, *runners_combination)
                    results = tournament.start()
                    for name, result in results.items():
                        results[name] = result.name
                    self.all_results[len(self.all_results) + 1] = results

                    # Вывод информации о текущей гонке
                    print(f"\nДистанция: {distance}м, Участники: {[runner.name for runner in runners_combination]}")
                    print(f"Результаты: {results}")

                    # Проверяем условия
                    sorted_results = sorted(results.keys(), key=lambda x: results[x].speed, reverse=True)

                    # Проверяем, что самый быстрый бегун на первом месте и самый медленный на последнем
                    fastest_runner = sorted_results[0]
                    slowest_runner = sorted_results[-1]

                    self.assertTrue(fastest_runner == results[fastest_runner].name, 
                                    f"Ошибка: {results[fastest_runner].name} не на первом месте на {distance}м")
                    self.assertTrue(slowest_runner == results[slowest_runner].name,
                                    f"Ошибка: {results[slowest_runner].name} не на последнем месте на {distance}м")

if __name__ == '__main__':
    unittest.main()

from runner_and_tournament import Runner, Tournament
import unittest
import itertools

class TournamentTest(unittest.TestCase):

    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runners = [
            Runner("Усэйн", speed=10),
            Runner("Андрей", speed=9),
            Runner("Ник", speed=3),
        ]

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_all_races(self):
        distances = [50, 100, 150]  # Определите возможные дистанции
        for distance in distances:
            for group in range(2, len(self.runners) + 1):
                for runners_combination in itertools.combinations(self.runners, group):
                    tournament = Tournament(distance, *runners_combination)
                    results = tournament.start()
                    for name, result in results.items():
                        results[name] = result.name
                    self.all_results[len(self.all_results) + 1] = results

                    # Вывод информации о текущей гонке
                    print(f"\nДистанция: {distance}м, Участники: {[runner.name for runner in runners_combination]}")
                    print(f"Результаты: {results}")

                    # Проверяем условия
                    sorted_results = sorted(runners_combination, key=lambda x: x.speed, reverse=True)

                    # Получаем имена участников
                    result_names = [runner.name for runner in sorted_results]

                    # Проверяем, что самый быстрый бегун на первом месте и самый медленный на последнем
                    fastest_runner = result_names[0]
                    slowest_runner = result_names[-1]

                    self.assertTrue(fastest_runner == results[fastest_runner], 
                                    f"Ошибка: {fastest_runner} не на первом месте на {distance}м")
                    self.assertTrue(slowest_runner == results[slowest_runner],
                                    f"Ошибка: {slowest_runner} не на последнем месте на {distance}м")

if __name__ == '__main__':
    unittest.main()
