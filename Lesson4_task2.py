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

### Немного доделанный Алгоритм из инета

def speedynumb(n):
    mass_simple = [2]
    for i in range(3, n+1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        else:
            flag = 0
            for j in mass_simple:
                if (i % j == 0):
                    flag += 1
                    break
            if (flag == 0):
                mass_simple.append(i)
    return(mass_simple)

# Lesson4_task2.speedynumb(20)
# 1000 loops, best of 3: 7.93 usec per loop
# Lesson4_task2.speedynumb(100)
# 1000 loops, best of 3: 58.1 usec per loop
# Lesson4_task2.speedynumb(1000)
# 1000 loops, best of 3: 1.97 msec per loop

#cProfile.run('speedynumb(20)')
# 1    0.000    0.000    0.000    0.000 Lesson4_task2.py:54(speedynumb)
# 7    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#cProfile.run('speedynumb(100)')
# 1    0.000    0.000    0.000    0.000 Lesson4_task2.py:54(speedynumb)
# 24    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#cProfile.run('speedynumb(1000)')
# 1    0.003    0.003    0.003    0.003 Lesson4_task2.py:54(speedynumb)
# 167    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# timeit почему-то показал увеличение времени выполнения, хотя должно быть
# меньше. Результат мне непонятен.

#print(bolter(100))
#print(speedynumb(100))

