#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача 2.
# Написать два алгоритма нахождения i-го по счёту простого числа.
# - Без использования Решета Эратосфена;
# - Использовать алгоритм решето Эратосфена

import cProfile

### Алгоритм и код "Решето Эратосфена" из лекции №2
def bolter(n):
    a = [0] * n
    for i in range(n):
        a[i] = i

    a[1] = 0
    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1

    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a
    return(b)
# Lesson4_task2.bolter(20)
# 1000 loops, best of 3: 12.9 usec per loop
# Lesson4_task2.bolter(100)
# 1000 loops, best of 3: 56.5 usec per loop
# Lesson4_task2.bolter(1000)
# 1000 loops, best of 3: 643 usec per loop

# cProfile.run('bolter(20)')
# 1    0.000    0.000    0.000    0.000 Lesson4_task2.py:12(bolter)
# 8    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# cProfile.run('bolter(100)')
# 1    0.000    0.000    0.000    0.000 Lesson4_task2.py:12(bolter)
# 25    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#cProfile.run('bolter(1000)')
# 1    0.001    0.001    0.001    0.001 Lesson4_task2.py:12(bolter)
# 168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

#print(bolter(20))
