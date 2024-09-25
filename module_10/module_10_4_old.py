# Домашнее задание по теме "Очереди для обмена данными между потоками."
# Назаров ПВ
# module_10_4_old.py

import threading
import time
import random

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Cafe:
    def __init__(self, tables):
        self.queue = []
        self.tables = tables

    def customer_arrival(self):
        customer_id = 1
        while customer_id <= 20:
            customer = Customer(customer_id)
            self.serve_customer(customer)
            customer_id += 1
            time.sleep(1)

    def serve_customer(self, customer):
        print(f"Посетитель номер {customer.id} прибыл")
        free_table = self.find_free_table()
        if free_table:
            free_table.is_busy = True
            print(f"Посетитель номер {customer.id} сел за стол {free_table.number}")
            customer.start()
        else:
            self.queue.append(customer)
            print(f"Посетитель номер {customer.id} ожидает свободный стол")

    def find_free_table(self):
        for table in self.tables:
            if not table.is_busy:
                return table
        return None

    def customer_finished(self, customer):
        for table in self.tables:
            if table.is_busy:
                table.is_busy = False
                print(f"Посетитель номер {customer.id} покушал и ушёл")
                if self.queue:
                    next_customer = self.queue.pop(0)
                    print(f"Посетитель номер {next_customer.id} вышел из очереди и сел за стол {table.number}")
                    next_customer.start()
                return

class Customer(threading.Thread):
    def __init__(self, id):
        super().__init__()
        self.id = id

    def run(self):
        time.sleep(random.uniform(3, 10))
        cafe.customer_finished(self)

if __name__ == "__main__":
    table1 = Table(1)
    table2 = Table(2)
    table3 = Table(3)
    tables = [table1, table2, table3]
    cafe = Cafe(tables)

    customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
    customer_arrival_thread.start()
    customer_arrival_thread.join()
