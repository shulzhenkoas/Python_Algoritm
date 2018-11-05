#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача 1.
# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

multiples = [0 for _ in range(0, 10)]

for m in range(2, 10):
    n = m
    while n < 100:
        if n % m == 0:
            multiples[m] += 1
        n += 1

print('В диапазоне натуральных чисел от "2" до "99"')
for i in range(2, 10):
    print('\tчислу "{}" кратны "{}" чисел'.format(i, multiples[i]))
