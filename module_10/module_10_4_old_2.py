# Домашнее задание по теме "Очереди для обмена данными между потоками."
# Назаров ПВ
# module_10_4_old_2.py

import threading
import time
import queue

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables
        self.customer_treads = []

    def customer_arrival(self):
        for i in range(1,21):
            print(f'Посетитель номер {i} прибыл.')
            self.serve_customer(i)
            time.sleep(1)

    def serve_customer(self, customer):
        free_table = False
        for table in tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"Посетитель номер {customer} сел за стол {table.number}.")
                customer_thr = Customer(customer, self, self.queue, table)
                customer_thr.start()
                self.customer_treads.append(customer_thr)
                free_table = True
                return

        if not free_table:
            self.queue.put(customer)
            print(f"Посетитель номер {customer} ожидает свободный стол.")


class Customer(threading.Thread):
    def __init__(self, number, cafe, queue, table):
        super().__init__()
        self.number = number
        self.cafe = cafe
        self.queue = queue
        self.table = table

    def run(self):
        time.sleep(5)
        print(f"Посетитель номер {self.number} покушал и ушел.")
        self.table.is_busy = False
        if not self.queue.empty():
            next_customer = self.queue.get()
            self.cafe.serve_customer(next_customer)

tables = []
for i in range(1,4):
    tables.append(Table(i))

cafe = Cafe(tables)

th1 = threading.Thread(target=cafe.customer_arrival)
th1.start()
th1.join()
