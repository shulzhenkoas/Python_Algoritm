#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача 1.
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
#
# Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания
# первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

import cProfile
import random

AMOUNT = 20

mass_elem = [random.randint(1, 100) for _ in range(AMOUNT)]
idx_min = idx_max = 0

for i in range(len(mass_elem)):
    if mass_elem[idx_max] <= mass_elem[i]:
        idx_max = i
    if mass_elem[idx_min] > mass_elem[i]:
        idx_min = i

print('Индекс минимального элемента "{}"\n'
      'Индекс максимального элемента "{}"'
      .format(idx_min, idx_max))
print('\nНачальный массив:\n{}'.format(mass_elem))
mass_elem[idx_min], mass_elem[idx_max] = mass_elem[idx_max], mass_elem[idx_min]
print('Измененный массив:\n{}'.format(mass_elem))