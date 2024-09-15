# Домашнее задание по теме "Оператор "with".
# Назаров ПВ
# module_7_3.py

from re import sub

class WordsFinder():
    def __init__(self, *name):
        self.file_names = name

    def get_all_words(self):
        self.all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                str_word = file.read().lower()
                str_word = sub(r"[,?!.\n=:;—]", " ", str_word)
            self.all_words[file_name] = str_word.split()
        return self.all_words

    def find(self, word):
        index_words = {}
        for file_name, str_word in self.all_words.items():
           # index = str_word.index(word.lower()) + 1
            index_words[file_name] = str_word.index(word.lower()) + 1
        return index_words

    def count(self, word):
        count_words = {}
        #count_word = 0
        for file_name, str_word in self.all_words.items():
            #count_word += str_word.count(word.lower())
            count_words[file_name] = str_word.count(word.lower())
        return count_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

# Дополнительные проверки
print()
print('Дополнительные проверки')
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

print()
finder1 = WordsFinder('Rudyard Kipling - If.txt', )
print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))

print()
finder1 = WordsFinder('Mother Goose - Monday’s Child.txt', )
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))

print()
print('Дополнительные проверки на все файлы')
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
