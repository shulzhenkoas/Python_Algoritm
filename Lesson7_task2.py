#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача 2.
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

NUMBER = 23
idx = 0
mass_elem = []
while idx < NUMBER:
    spam = random.uniform(0, 50)
    if spam < 50:
        mass_elem.append(round(spam, 3))
        idx += 1
#mass_elem = [round(random.uniform(0, 50), 3) for _ in range(NUMBER)]
print(mass_elem)

### Алгоритм и код взял из инета
def merge_sorting(mass_elem):

    if len(mass_elem) < 2:
        return mass_elem
    middle = int(len(mass_elem) / 2)
    mass_left = merge_sorting(mass_elem[:middle])
    mass_right = merge_sorting(mass_elem[middle:])

    return merge(mass_left, mass_right)

def merge(mass_left, mass_right):

    result = []
    i ,j = 0, 0
    while i < len(mass_left) and j < len(mass_right):
        if mass_left[i] <= mass_right[j]:
            result.append(mass_left[i])
            i += 1
        else:
            result.append(mass_right[j])
            j += 1
    result += mass_left[i:]
    result += mass_right[j:]

    return result

print(merge_sorting(mass_elem))
