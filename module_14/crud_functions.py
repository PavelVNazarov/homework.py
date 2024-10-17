# Домашнее задание по теме "План написания админ панели"
# Назаров ПВ
# module_14_4 crud_functions.py

import sqlite3

def initiate_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL,
            url TEXT,
            short_name TEXT NOT NULL )
    ''')
    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT title, description, price, url, short_name FROM Products')
    products = cursor.fetchall()
    conn.close()
    return products

def insert_products(products_info):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.executemany('''
        INSERT INTO Products (title, description, price, url, short_name) VALUES (?, ?, ?, ?, ?)
    ''', products_info)

    conn.commit()
    conn.close()

# Пример заполнения базы данными
if __name__ == "__main__":
    initiate_db()

    products_info = [
        ["California Gold Nutrition Baby Vitamin D3 Liquid","Вариант для самых маленьких. Также в составе есть ДГК (докозагексаеновая кислота) — омега-3 жирная кислота, необходимая для формирования мозга, нервной системы и зрения у ребенка.","100","https://ltdfoto.ru/images/2024/10/17/babyd34c24ca37eabfb2b4.png","BabyD3"],
        ["California Gold Nutrition Omega-3 Premium Fish Oil","Капсулы с рыбьим жиром омега-3 премиального качества. Они содержат ключевые омега-3 жирные кислоты, такие как ДГК и ЭПК.","100","https://ltdfoto.ru/images/2024/10/17/omega324684226cd955fae.png","Omega-3"],
        ["Магний хелат Эвалар","Биологически активная добавка в таблетках. Этот магний в хелатной форме также хорошо усваивается организмом.","100","https://ltdfoto.ru/images/2024/10/17/magnibed42d251ce0a26b.png","Magni"],
        ["GLS Коллаген 1000","Биологически активная добавка (БАД) к пище с гидролизатом рыбного коллагена.","100","https://ltdfoto.ru/images/2024/10/17/collagen5263a67645df4975.png","Collagen"],
    ]
    insert_products(products_info)
