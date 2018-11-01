#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача 4.
# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

n = abs(int(input('Введите количество элементов ряда: ')))
sum =float(0)
elem = float(1)
row = list()

if n != 0:
    while n > 0:
        sum = sum + elem
        row.append(elem)
        elem = -0.5 * elem
        n -= 1
    print('Сумму элементов ряда чисел: "{}" равна "{}"'.format(row, sum))
else:
    print('Это пустой ряд!')
