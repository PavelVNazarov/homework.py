# Домашнее задание по теме "Очереди для обмена данными между потоками."
# Назаров ПВ
# module_10_4_old.py

import threading
import time
import random
import queue

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables

    def customer_arrival(self):
        customer_num = 1
        while customer_num <= 20:
            customer = Customer(customer_num)
            self.serve_customer(customer)
            customer_num += 1
            time.sleep(4)

    def serve_customer(self, customer):
        print(f"Посетитель номер {customer.num} прибыл")
        free_table = self.find_free_table()
        if free_table:
            free_table.is_busy = True
            print(f"Посетитель номер {customer.num} сел за стол {free_table.number}")
            customer.start()
        else:
            self.queue.put(customer)
            print(f"Посетитель номер {customer.num} ожидает свободный стол")

    def find_free_table(self):
        for table in self.tables:
            if not table.is_busy:
                return table
        return None

    def customer_finished(self, customer):
        for table in self.tables:
            if table.is_busy:
                table.is_busy = False
                print(f"Посетитель номер {customer.num} покушал и ушёл")
                if not self.queue.empty():
                    next_customer = self.queue.get()
                    print(f"Посетитель номер {next_customer.num} вышел из очереди и сел за стол {table.number}")
                    next_customer.start()
                return

class Customer(threading.Thread):
    def __init__(self, num):
        super().__init__()
        self.num = num

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
