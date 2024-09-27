# Домашнее задание по теме "Обзор сторонних библиотек Python"
# Назаров ПВ
# module_11_1

import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()
print(data)


import pandas as pd

# Считываем данные из CSV файла
df = pd.read_csv('data.csv')

# Вывести первые 5 строк
print(df.head())

# Посчитать среднее значение по определенному столбцу
average = df['column_name'].mean()
print(f'Среднее значение: {average}')



import matplotlib.pyplot as plt

# Пример данных
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

plt.plot(x, y, marker='o')
plt.title("Пример графика")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
