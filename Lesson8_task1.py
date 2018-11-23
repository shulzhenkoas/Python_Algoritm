# __author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача 1.
# Определение количества различных подстрок с использованием хеш-функции. Пусть дана строка S длиной N.
# Например, состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
# Для решения задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib или встроенную функцию hash()

from random import choice
from string import ascii_lowercase

def string_gen(numb):
    string = ''.join([choice(ascii_lowercase) for _ in range(numb)])
    return string

def calc_hash(string):
    spam_diff = []
    len_string = len(string)
    for i in range(1, len_string):
        for j in range(0, len_string - i + 1):
            sub_string = string[j:j + i]
#            print(sub_string)
            hash_sub = hash(sub_string)
            if hash_sub not in spam_diff:
                spam_diff.append(hash_sub)
    return len(spam_diff)

eggs = string_gen(5)
print('В исходной строке:\n"{}"\n разных подстрок - "{}".'.format(eggs, calc_hash(eggs)))
