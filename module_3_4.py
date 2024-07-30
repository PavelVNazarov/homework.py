# Самостоятельная работа по уроку "Произвольное число параметров".
# Назаров ПВ

def single_root_words(root_word,*other_words):
    same_words = []
    for i in range(0,len(other_words)):
        if other_words[i].lower() in root_word.lower():
            same_words.append(other_words[i])
        if root_word.lower() in other_words[i].lower():
            same_words.append(other_words[i])

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)  