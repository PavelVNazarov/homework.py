# Домашнее задание по теме "Простые Юнит-Тесты"
# Назаров ПВ
# tests_12_1_old.py

import unittest
from main import Student


class TestStudentMovement(unittest.TestCase):

    def test_walk_distance(self):
        student = Student('Ходяев')
        for _ in range(10):
            student.walk()
        self.assertEqual(student.distance, 500,
                         f"Дистанции не равны {student.distance} != 500")

    def test_run_distance(self):
        student = Student('Проверяев')
        for _ in range(10):
            student.run()
        self.assertEqual(student.distance, 1000,
                         f"Дистанции не равны {student.distance} != 1000")

    def test_compete(self):
        runner = Student('Быстров')
        walker = Student('Неспешнев')

        for _ in range(10):
            runner.run()

        for _ in range(10):
            walker.walk()

        self.assertGreater(runner.distance, walker.distance,
                           f"{runner.name} должен преодолеть дистанцию больше, чем {walker.name}")


if __name__ == '__main__':
    unittest.main()


# module_main_for12_1_old.py
# 
# 
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.distance = 0
# 
#     def run(self):
#         self.distance += 10
# 
#     def walk(self):
#         self.distance += 5
# 
#     def __str__(self):
#         return self.name
