# Домашнее задание по теме "Оператор "with".
# Назаров ПВ
# module_7_3.py

class WordsFinder():
    def __init__(self,*name):
        self.file_names = list(name)

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i) as file:
                for j in file:
                    all_words = {i: [j.lower()]}
        return all_words

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
