#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача 4.
# Определить, какое число в массиве встречается чаще всего.
#
# VirualBox под Windows 8.1 64-bit
# Linux debian 4.9.0-7-686 #1 SMP Debian 4.9.110-3+deb9u2 (2018-08-13) i686 GNU/Linux 32-bit

import random
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

AMOUNT = 30

mass_elem = [random.randint(1, 10) for _ in range(AMOUNT)]
data_base = {key: 0 for key in set(mass_elem)}
maximum_value = 0

for m in data_base.keys():
    for n in mass_elem:
        if m == n:
            data_base[m] += 1
        if maximum_value <= data_base[m]:
            maximum_value = data_base[m]

#print(sorted(mass_elem))
#print(data_base)
#print(maximum_value)

print('В массиве:\n{}\nчаще всего встречаются следующие числа:'.format(mass_elem))
for m in data_base.keys():
    if data_base[m] == maximum_value:
        print('\t"{}" встречается "{}" раз(а)'.format(m, data_base[m]))

### Ниже код "первоклассника"
out_mem = OrderedDict()
size_all_obj = 0

all_objects = (AMOUNT, mass_elem, data_base, maximum_value, set(mass_elem))
for idx in all_objects:
    show_size(idx)

print('\nВ программе используются "{}" объект(а/ов):'.format(len(out_mem)))
for key, value in out_mem.items():
    print(key)
    size_all_obj += value
print('Общий объем занимаемой памяти "{}" байт.'.format(size_all_obj))

### Здесь все объекты типа int.
### Как видно из вывода что для list, что для dict Python старается хранить только уникальные объекты.
### Так как ключи в dict типа int, то Python так же оптимизирует их хранение.
### Для dict отлавливал, что цифры повторялись, почему не понял.
###
### Временные переменные в циклах не считал и генераторах не считал
