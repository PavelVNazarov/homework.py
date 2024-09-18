# Домашнее задание по теме "Итераторы"
# Назаров ПВ
# module_9_5_old.py

class EvenNumbers():
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end

    def __iter__ (self):
       return self

    def __next__(self):
        if self.start < self.end:
            self.start += 2
            return self.start-2
        else:
            raise StopIteration()


en = EvenNumbers(10, 25)
for i in en:
	print(i)
