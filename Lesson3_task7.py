#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача 7.
# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.

import random

AMOUNT = 20

mass_elem = [random.randint(1, 100) for _ in range(AMOUNT)]
print('Массив элементов:\n{}'.format(mass_elem))
#print(sorted(mass_elem))

for m in [0, 1]:
    for n in range(m, len(mass_elem)):
        if mass_elem[m] > mass_elem[n]:
            mass_elem[m], mass_elem[n] = mass_elem[n], mass_elem[m]
print('Два наименьшиз элемента массива "{}" и "{}"'.format(mass_elem[0], mass_elem[1]))
