# Домашнее задание по теме "Простые Юнит-Тесты"
# Назаров ПВ
# tests_12_1.py

from unittest import TestCase, main
from runner import Runner

class RunnerTest(TestCase):

    def test_walk(self):
        walker = Runner('Turtle')
        for _ in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50,
                         f"Дистанции не равны {walker.distance} != 50")

    def test_run(self):
        runner = Runner('Rabbit')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100,
                         f"Дистанции не равны {runner.distance} != 100")

    def test_challenge(self):
        runner = Runner('Rabbit')
        walker = Runner('Turtle')

        for _ in range(10):
            runner.run()
            walker.walk()
            
       # for _ in range(10):
       #     walker.walk()

        self.assertNotEqual(runner.distance, walker.distance,
                           runner.distance == walker.distance)

if __name__ == '__main__':
    main()
