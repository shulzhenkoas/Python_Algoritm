#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача 9.
# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

print('Введите три числа:')
a = float(input('"Первое число" - '))
b = float(input('"Второе число" - '))
c = float(input('"Третье число" - '))

if a != b and b != c and a != c:
    if a > b:
        if a > c:
            if b > c:
                aver = b
            else:
                aver = c
        else:
            aver = a
    else:
        if b > c:
            if a > c:
                aver = a
            else:
                aver = c
        else:
            aver = b
    print('\nСреднее число "{}"'.format(aver))
else:
    print('\nВсе числа должны быть разными!')

