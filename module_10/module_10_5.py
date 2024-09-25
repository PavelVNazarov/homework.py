# Домашнее задание по теме "Многопроцессное программирование"
# Назаров ПВ
# module_10_5.py

import datetime
import multiprocessing

def read_info(name):
    all_data = []  # без этого можно обойтись
    with open(name, encoding='utf-8') as file:
        all_data = file.readlines()
filenames = [f'./file {number}.txt' for number in range(1, 5)]

# 0:00:09.261991 Линейный вызов
# 0:00:05.229906 Многопроцессный


# Линейный вызов
# start = datetime.datetime.now()
# for file in filenames:
#     read_info(file)
#
# end = datetime.datetime.now()
# print(end-start)


# Многопроцессный
if __name__ == '__main__':
    with multiprocessing.Pool(processes=6) as pool:
        start = datetime.datetime.now()
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end-start)
