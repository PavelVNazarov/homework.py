# Домашнее задание по теме "Интроспекция"
# Назаров ПВ
# module_11_3

class Tree:
    def __init__(self, name: str, bearing = False):
        self.name = name
        self.bearing = bearing

class AppleTree(Tree):
    def __init__(self, name, bearing):
        super().__init__(name, bearing)
        self.mass = 0
        self.count = 0

    def harvest(self):
        harvest_amount = self.count * self.mass * 0.001
        print(f'Урожай {self.name} с одной яблони {harvest_amount} кг!')


golden_apple = AppleTree('Golden', True)
golden_apple.count = 120
golden_apple.count = 2500
golden_apple.harvest()

def introspection_info(obj):
    number_info = {}
    number_info['type'] = type(obj)
    number_info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]
    number_info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')]
    number_info['modules'] = [module for module in dir(obj) if module.startswith('__')]

    return number_info

number_info = introspection_info(golden_apple)
print(number_info)
