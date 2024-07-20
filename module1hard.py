# Дополнительное практическое задание по модулю: "Базовые структуры данных."
# Назаров ПВ
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_of_student =sorted(students)
average_grades = [round(sum(grades[0])/len(grades[0]),2), round(sum(grades[1])/len(grades[1]),2),round(sum(grades[2])/len(grades[2]),2), round(sum(grades[3])/len(grades[3]),2),round(sum(grades[4])/len(grades[4]),2)]
grades_of_student = dict(zip(list_of_student, average_grades))
print(grades_of_student)