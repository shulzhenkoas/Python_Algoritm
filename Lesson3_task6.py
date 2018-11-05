#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача 6.
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

AMOUNT = 10
TEXT = 'Сумма элементов находящихся между минимальным и максимальным элементом равна'

mass_elem = [random.randint(1, 100) for _ in range(AMOUNT)]
basket = idx_min = idx_max = 0

for i in range(len(mass_elem)):
    if mass_elem[idx_max] <= mass_elem[i]:
        idx_max = i
    if mass_elem[idx_min] > mass_elem[i]:
        idx_min = i

print('Массив:\n{}'.format(mass_elem))
print('Индекс минимального элемента "{}"\n'
      'Индекс максимального элемента "{}"\n'
      .format(idx_min, idx_max))

if idx_max > idx_min:
    for i in range(idx_min + 1, idx_max):
        basket += mass_elem[i]
else:
    for i in range(idx_max + 1, idx_min):
        basket += mass_elem[i]

print('{} "{}"'.format(TEXT, basket))
