#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача 8.
# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
year = int(input('Введите год: '))

if (year % 4 != 0):
    print('Это невисокосный год.')
elif (year % 100 == 0) and (year % 400 != 0):
    print('Это невисокосный год.')
else:
    print('Это високосный год.')