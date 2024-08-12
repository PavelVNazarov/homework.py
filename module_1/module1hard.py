# Дополнительное практическое задание по модулю: "Базовые структуры данных."
# Назаро ПВ
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# идеальный ответ average_rating = {'Aaron': 4.5, 'Bilbo': 3.0, 'Johnny': 4.0,, 'Khendrik': 4.5, 'Steve': 3.0}
average_grabes = [round(sum(grades[0]) / len(grades[0]),2), round(sum(grades[1]) / len(grades[1]),2), round(sum(grades[2]) / len(grades[2]),2), round(sum(grades[3]) / len(grades[3]),2), round(sum(grades[4]) / len(grades[4]),2) ] # список с оценками студентов
list_of_students = sorted(students) # список с именами студентов
average_rating = dict(zip(list_of_students, average_grabes))
print(average_rating)
