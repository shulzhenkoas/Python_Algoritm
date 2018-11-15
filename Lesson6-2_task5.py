#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача 5.
# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.
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

START_ASCII = 32
END_ASCII = 127
text = ''
pair = 0

for i in range(START_ASCII, END_ASCII + 1):
    ### Добавлено для понимания формирования строковой переменной
    print(i)
    print('alias "text" = ', sys.getrefcount(text))
    print('size "text" =', sys.getsizeof(text))
    print('addr "text" =', id(text))
    ###
    text += '"{}":"{}"'.format(i, chr(i))
    pair += 1
    if pair == 10:
        text += '\n'
        pair = 0
    else:
        text += '\t'

#print('Таблица ASCII символов от "{}" до "{}":\n{}'.format(START_ASCII, END_ASCII, text))

### Ниже код "первоклассника"
out_mem = OrderedDict()
size_all_obj = 0

all_objects = (START_ASCII, END_ASCII, text, pair)
for idx in all_objects:
    show_size(idx)

print('\nВ программе используются "{}" объект(а/ов):'.format(len(out_mem)))
for key, value in out_mem.items():
    print(key)
    size_all_obj += value
print('Общий объем занимаемой памяти "{}" байт.'.format(size_all_obj))

### Переменной "text" типа str при создании соответствуют 137 ссылок, потом при добавлении элементов - 2,
### но в итоге откуда-то берутся 7. Как так получается?
###
### До 637 байта (ASCII = 100) память переменной "text" выделяется по 9 байт, после по 10 байт.
### Это как-то связано с тем, что код ASCII стал трехзначным.
###
### До элемента с ASCII = 87 size=520 адреса памяти объекта "text" разные, а потом адрес становиться "меньше"
### и не меняется (например был 3072730656 стал 13337208). Почему так?
###
### Остальные переменные int - как в предыдущем задании.
###
### А можно ка-нибудь отловить момент, когда старая строка копируется в новую?
### Должно ведь быть двойное использование памяти
###
### Временные переменные в циклах не считал
