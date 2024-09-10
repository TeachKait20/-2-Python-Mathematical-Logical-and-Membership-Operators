# Проверка символов в строках и сравнение строк
# Внимательно изучите результат выполнения кода

greets = "Hello, my name is Bobby!"

print('Проверка строки в переменной greets на то, что в ней есть (in): ')
print('t' in greets)  # t нет в строке
print('is' in greets)  # is есть в строке
print(' ' in greets)  # пробел есть в строке

print() # пустой print даст пробел в консоли. Пробелы в самом коде (пропущенные строчки) не дадут такого эффекта.

print('Проверка строки в переменной greets на то, чего в ней нет (not in): ')
print('t' not in greets)  # t нет в строке
print('is' not in greets)  # is есть в строке
print(' ' not in greets)  # пробел есть в строке

print()
print('Сравнение строк: ')

leaves = "Bye! See you tomorrow?"  # новая переменная со строкой

print(greets == leaves)  # на одинаковость
print(greets != leaves)  # на разность

print()
print('Проверка на количество символов: ')
print('В строке greets: ', len(greets), 'символов.')
print('В строке leaves: ', len(leaves), 'символов.')
print(len(greets) > len(leaves))
print(len(greets) >= len(leaves))
print(len(greets) < len(leaves))
print(len(greets) <= len(leaves))
print(len(greets) == len(leaves))
print(len(greets) != len(leaves))


