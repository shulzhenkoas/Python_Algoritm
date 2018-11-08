#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача 1.
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
#
# Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания
# первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

import cProfile
### Решение из домашнего задания
def massivius(amount):
    import random
    mass_elem = [random.randint(1, 100) for _ in range(amount)]
    return mass_elem

def minimax(amount):
    mass_elem = massivius(amount)
    idx_min = idx_max = 0

    for i in range(len(mass_elem)):
        if mass_elem[idx_max] <= mass_elem[i]:
            idx_max = i
        if mass_elem[idx_min] > mass_elem[i]:
            idx_min = i
    mass_elem[idx_min], mass_elem[idx_max] = mass_elem[idx_max], mass_elem[idx_min]
    return(idx_min, idx_max, mass_elem)

# Lesson4_task1.minimax(20)
# 1000 loops, best of 3: 54 usec per loop
# Lesson4_task1.minimax(100)
# 1000 loops, best of 3: 230 usec per loop
# Lesson4_task1.minimax(1000)
# 1000 loops, best of 3: 2.43 msec per loop

# cProfile.run('minimax(20)')
# 1    0.000    0.000    0.036    0.036 Lesson4_task1.py:19(minimax)
# 1289 function calls (1261 primitive calls) in 0.040 seconds
# cProfile.run('minimax(100)')
# 1    0.000    0.000    0.038    0.038 Lesson4_task1.py:19(minimax)
# 1707 function calls (1679 primitive calls) in 0.038 seconds
# cProfile.run('minimax(1000)')
# 1    0.000    0.000    0.043    0.043 Lesson4_task1.py:19(minimax)
# 6498 function calls (6470 primitive calls) in 0.043 seconds

# Время замены мест минимального и максимального элементов равно
# времени его генерации. Не понимаю почему timeit показывает одно время
# с cProfile больше.

### С использованием встоенных функций из лекции №3
def integrated(amount):
    mass_elem = massivius(amount)
    min_num = min(mass_elem)
    max_num = max(mass_elem)
    idx_min = mass_elem.index(min_num)
    idx_max = mass_elem.index(max_num)
    mass_elem[idx_min], mass_elem[idx_max] = mass_elem[idx_max], mass_elem[idx_min]
    return(idx_min, idx_max, mass_elem)

# Lesson4_task1.integrated(20)
# 1000 loops, best of 3: 48.6 usec per loop
# Lesson4_task1.integrated(100)
# 1000 loops, best of 3: 224 usec per loop
# Lesson4_task1.integrated(1000)
# 1000 loops, best of 3: 2.21 msec per loop

#cProfile.run('integrated(20)')
# 1    0.000    0.000    0.027    0.027 Lesson4_task1.py:51(integrated)
# 1289 function calls (1261 primitive calls) in 0.027 seconds
#cProfile.run('integrated(100)')
# 1    0.000    0.000    0.027    0.027 Lesson4_task1.py:51(integrated)
# 1718 function calls (1690 primitive calls) in 0.027 seconds
#cProfile.run('integrated(1000)')
# 1    0.000    0.000    0.026    0.026 Lesson4_task1.py:51(integrated)
# 6455 function calls (6427 primitive calls) in 0.026 seconds

# cProfile показывает, что время выполнения функции замены мест минимального
# и максимального элементов почему-то не растет с увеличением количества
# элементов массива

#print(*minimax(20), sep='\n')
#print(*integrated(20), sep='\n')