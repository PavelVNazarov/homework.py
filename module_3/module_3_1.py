# Домашняя работа по уроку "Пространство имён"
# Назаров ПВ
calls = 0

def count_calls(): 
    global calls
    calls += 1
    

def string_info(string):
    count_calls()
    my_tupl = (len(string), string.upper(), string.lower())
    return my_tupl
  
def is_contains(string,list_to_search):
    count_calls()
    i = 0
    while i < len(list_to_search):
        if list_to_search[i].lower() == string.lower():
            return True
            break
        i += 1 
    if i == len(list_to_search):
      return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
