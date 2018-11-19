# __author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача 1.
# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована
# в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import random

def bubble_sorting(mass_elem):
    n = len(mass_elem)
    while n > 0:
        flag = 0
### По фэнщуй лучше использовать в range - len(mass_elem) или константу NUMBER (не применительно к функции)?
### Хотя NUMBER можно и передать внутрь my_sorting.
### Возможен случай, что генератор сгенерирует меньше элементов чем задано?
        for i in range(len(mass_elem) - 1, len(mass_elem)-n, -1):
            if mass_elem[i] > mass_elem[i-1]:
                mass_elem[i],mass_elem[i-1] = mass_elem[i-1],mass_elem[i]
                flag = 1
#        print(mass_elem)
        if flag == 0:
            break
        n -= 1
    return mass_elem

NUMBER = 23
mass_elem = [random.randint(-100, 99) for _ in range(NUMBER)]
print(mass_elem)
print(bubble_sorting(mass_elem))
