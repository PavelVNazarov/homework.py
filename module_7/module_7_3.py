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
        str_word = str_word.replace('\n',' ')
        str_word = str_word.replace(',',' ')
        str_word = str_word.replace('.',' ')
        str_word = str_word.replace('=',' ')
        str_word = str_word.replace('!',' ')
        str_word = str_word.replace('?',' ')
        str_word = str_word.replace(';',' ')
        str_word = str_word.replace(':',' ')
        str_word = str_word.replace(' - ',' ')
        str_word = str_word.lower()
        str_word = str_word.split()
        all_words = {i: str_word }
        return all_words

    def find(self, word):
        index_words = []
        str_word = self.get_all_words()
        for i,j in str_word.items():
            #if word in j:
            index = j.index(word.lower())+1
            break
        index_words = {i: index}
        return index_words

    # def count(self, word):
    #     count_words = {}
    #     count_word = 0
    #     #str_word = finder2.get_all_words()
    #     for i in self.file_names:
    #         with open(i, encoding = 'utf-8') as file:
    #             for j in file:
    #                 str_word +=''.join(j.split())
    #                 str_word = str_word.lower()
    #                 count_word = j.count(word.lower())
    #     count_words = {i: count_word}
    #     return count_words
        
    def count(self, word):
        all_words = {}
        count_word = 0
        str_word =''
        for i in self.file_names:
            with open(i, encoding = 'utf-8') as file:
                for j in file:
                    str_word +=''.join(j.split())
                    str_word = str_word.lower()
                    count_word = str_word.count(word.lower())
        all_words = {i: count_word}
        return all_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

finder1 = WordsFinder('Rudyard Kipling - If.txt',)

print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))

finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
      'Rudyard Kipling - If.txt',
      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
        
