# Домашнее задание по теме "Очереди для обмена данными между потоками."
# Назаров ПВ
# module_10_4_old.py

from time import sleep
import threading

#from random import randint
#lock = Lock()

class Table():
    def __init__(self, number: int, busy = True):
        self.number = number
        self.busy = busy

class Cafe():
    def __init__(self, tables):
        self.queue = []
        self.tables = tables

    def  customer_arrival(self):
        customer = Customer()
        for table in self.tables:
            if table.busy == True:
                self.queue.append(customer)
                print (f'Посетитель номер {self.queue.index(customer)} прибыл')
                self.serve_customer()
        sleep(1)

    def serve_customer(self):

        for table in self.tables:
            if table.busy == True:
                table.busy == False
                customer = self.queue.pop(0)
                print(f'Посетитель номер {customer} сел за стол {table.number}')
            else:
                print(f'Посетитель номер {customer} ожидает свободный стол.')
                self.queue.append(customer)
            sleep(5)

class Customer():
    pass

# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]
# Инициализируем кафе
cafe = Cafe(tables)
# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()
# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
