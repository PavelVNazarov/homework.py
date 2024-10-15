# Домашнее задание по теме "Выбор элементов и функции в SQL запросах"
# Назаров ПВ
# module_14_2.py

import sqlite3

# Создаем или подключаемся к базе данных not_telegram.db
conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

# Заполняем таблицу
users = []
for i in range(1, 11):
    users.append((f"User{i}", f"example{i}@gmail.com", i * 10, 1000))

cursor.executemany("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", users)

# Обновляем balance у каждой 2-й записи начиная с 1-й
cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 = 0")

# Удаляем каждую 3-ю запись начиная с 1-й
cursor.execute("DELETE FROM Users WHERE id % 3 = 1")

# Делаем выборку всех записей, где возраст не равен 60
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
results = cursor.fetchall()

# Выводим результат в нужном формате
for row in results:
    username, email, age, balance = row
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

# Подсчет общего количества записей
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

# Подсчет суммы всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0] or 0

# Вычисляем средний баланс
average_balance = all_balances / total_users if total_users else 0

# Выводим средний баланс
print(f"Средний баланс: {average_balance}")

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()
