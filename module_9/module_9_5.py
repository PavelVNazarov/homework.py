# Домашнее задание по теме "Итераторы"
# Назаров ПВ
# module_9_5.py

class StepValueError(ValueError):
    pass

class Iterator():
    def __init__(self, start, stop, step = 1):
        self.start = start
        self.stop = stop
        if step != 0:
            self.step = step
        else:
            StepValueError('шаг не может быть равен 0')

    def __iter__ (self):
        self.pointer = self.start
        return self

    def __next__(self):

        if self.pointer < self.start or self.pointer > self.stop:
            raise StopIteration()
        self.pointer += self.step
        return self.pointer

""""""

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
