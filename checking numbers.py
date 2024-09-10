# проверка и сравнение чисел

my_number = 15
your_number = 20

print('Равенства чисел: ')
print(my_number == your_number)  # равно ли
print(my_number != your_number)  # не равно ли

print()
print(my_number + your_number == 35)  # проверка ответа при математической операции двух чисел
print(my_number + your_number != 35)

print()
print('Проверка на кратность: ')
print(my_number % 3 == 0)  # не будет ли остатка при делении my_number на 3
print(my_number % 2 == 1)  # будет ли остаток при делении my_number на 2

print()
print('Сравнение чисел: ')
print(my_number > your_number)  # больше ли my_number, чем your_number
print(my_number <= your_number)  # меньше или равно my_number числу в your_number

print()
print('Арифметические операции: ')
print(my_number + your_number, my_number - your_number)
print(my_number, '*', your_number, '=', my_number * your_number)
