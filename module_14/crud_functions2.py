# Домашнее задание по теме "План написания админ панели"
# Назаров ПВ
# module_14_5 crud_functions2.py

import sqlite3

def initiate_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Создание таблицы Products
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
    )
    ''')
    
    # Создание таблицы Users
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL DEFAULT 1000
    )
    ''')
    
    conn.commit()
    conn.close()

def add_user(username, email, age):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO Users (username, email, age, balance)
    VALUES (?, ?, ?, ?)
    ''', (username, email, age, 1000))
    conn.commit()
    conn.close()

def is_included(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM Users WHERE username = ?
    ''', (username,))
    user = cursor.fetchone()
    conn.close()
    return user is not None

def get_all_products():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    conn.close()
    return products

# Перед запуском бота добавить записи в Products
def populate_initial_products():
    products = [
        ('Product 1', 'Description 1', 100),
        ('Product 2', 'Description 2', 200),
        ('Product 3', 'Description 3', 300),
        ('Product 4', 'Description 4', 400),
    ]
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.executemany('''
    INSERT INTO Products (title, description, price)
    VALUES (?, ?, ?)
    ''', products)
    conn.commit()
    conn.close()
