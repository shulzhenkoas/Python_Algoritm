#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача 4.
# Определить, какое число в массиве встречается чаще всего.

import random

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
