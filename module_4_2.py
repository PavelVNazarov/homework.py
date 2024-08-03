# Домашнее задание по уроку "Пространство имен"
# Назаров ПВ

def test_function():
  def inner_function():
    print('Я в области видимости функции test_function')

  inner_function()

print('Я вне функции test_function')
test_function()
inner_function()