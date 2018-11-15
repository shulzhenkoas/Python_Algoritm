#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача 5.
# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
#
# Подсчитать, сколько было выделено памяти под переменные. Проанализировать результат и определить программы
# с наиболее эффективным использованием памяти.
#
# VirualBox под Windows 8.1 64-bit
# Linux debian 4.9.0-7-686 #1 SMP Debian 4.9.110-3+deb9u2 (2018-08-13) i686 GNU/Linux 32-bit

import sys
from collections import OrderedDict

def show_size(x, level=0):
    text = '{} type = {}, size = {}, object = {}, id_mem = {}, alias = {}'\
        .format('\t' * level, type(x), sys.getsizeof(x), x, id(x), sys.getrefcount(x))
    out_mem[text] = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)

print('Введите две буквы аглийского алфавита от "a" до "z":')
char1 = input('"Первая буква" - ')
if 96 < ord(char1) < 123:
    char2 = input('"Вторая буква" - ')
    if 96 < ord(char2) < 123:
        print('\nСимвол "{}" является {} буквой английского алфавита.'.format(char1, ord(char1) - 96))
        print('Символ "{}" является {} буквой английского алфавита.'.format(char2, ord(char2) - 96))
        print('Между символами "{}" и "{}" "{}" букв английского алфавита.'.format(char1, char2, ord(char2) - ord(char1)))
    else:
        print('\nВторой символ не из указанного диапазона.')
else:
    print('\nПервый символ не из указанного диапазона.')

### Ниже код "первоклассника"
out_mem = OrderedDict()
size_all_obj = 0

all_objects = (char1, char2, ord(char1) - 96, ord(char2) - 96, ord(char2) - ord(char1))
### А можно как-то передать само название перменной в функцию (например char1), помимо ее значения?
for idx in all_objects:
    show_size(idx)

print('\nВ программе используются "{}" объект(а/ов):'.format(len(out_mem)))
for key, value in out_mem.items():
    print(key)
    size_all_obj += value
print('Общий объем занимаемой памяти "{}" байт.'.format(size_all_obj))

### Адреса памяти для переменных для int и str отличаются.
### Интересно, а как сборщик мусора Python работает с вычисляемыми значениями,
### которые не "сохраняются" (не "присватваются" переменным)?
