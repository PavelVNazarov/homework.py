# Домашнее задание по теме "Оператор "with".
# Назаров ПВ
# module_7_3.py

class WordsFinder():
    def __init__(self,*name):
        self.file_names = list(name)

    def get_all_words(self):
        all_words = {}
        str_word = ''
        for i in self.file_names:
            with open(i, encoding = 'utf-8') as file:
                for j in file:
                    str_word +=' '.join(j.split())
        str_word = str_word.split()
        all_words = {i: str_word }
        return all_words

    def find(self, word):
        all_words = []
        for i in self.file_names:
            with open(i, encoding = 'utf-8') as file:
                for j in file:
                    j = j.lower()
                    index = j.index(word.lower())
                    #if word.lower() in j.lower():
                    all_words = {i: index}
                    break
                    break
        return all_words

    def count(self, word):
        all_words = {}
        count_word = 0
        for i in self.file_names:
            with open(i, encoding = 'utf-8') as file:
                for j in file:
                    if word.lower() in j.lower():
                        count_word += 1
        all_words = {i: count_word}
        return all_words



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
        
