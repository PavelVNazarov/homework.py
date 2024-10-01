# Домашнее задание по теме "Простые Юнит-Тесты"
# Назаров ПВ
# module_12_1_old.py

import unittest
from main import Student  # Предположим, что класс Student находится в файле main.py


class TestStudentMovement(unittest.TestCase):

    def test_walk_distance(self):
        student = Student()
        for _ in range(10):
            student.walk()  # Предполагаем, что метод walk увеличивает дистанцию
        self.assertEqual(student.distance, 500,
                         f"Дистанции не равны {student.distance} != 500")

    def test_run_distance(self):
        student = Student()
        for _ in range(10):
            student.run()  # Предполагаем, что метод run увеличивает дистанцию
        self.assertEqual(student.distance, 1000,
                         f"Дистанции не равны {student.distance} != 1000")

    def test_compete(self):
        runner = Student()
        walker = Student()

        for _ in range(10):
            runner.run()

        for _ in range(10):
            walker.walk()

        self.assertGreater(runner.distance, walker.distance,
                           f"{runner.name} должен преодолеть дистанцию больше, чем {walker.name}")


if __name__ == '__main__':
    unittest.main()
