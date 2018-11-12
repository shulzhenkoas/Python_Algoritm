# __author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача 2.
# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как
# [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

hex_number = tuple('0123456789ABCDEF')
print(hex_number)

hex_var = deque()
for i in range(2):
    hex_var.append(deque(input('Введите ' + str(i+1) + '-ое число:').upper()))

dec_var = deque()
for var in hex_var:
    spam = 0
    idx = len(var) - 1
    for pos in var:
        spam += hex_number.index(pos) * (16 ** idx)
        idx -= 1
    dec_var.append(spam)

dec_var.append(dec_var[0] + dec_var[1])
#dec_var.append(dec_var[0] * dec_var[1])
dec_var.append(dec_var.popleft() * dec_var.popleft())
#print(dec_var)

while dec_var:
    spam = dec_var.popleft()
    spam_hex = deque()
    while spam != 0:
        spam_hex.appendleft(hex_number[spam % 16])
        spam //= 16
    hex_var.append(spam_hex)

del dec_var

print('"{}" + "{}" = "{}"'.format(''.join(hex_var[0]), ''.join(hex_var[1]), ''.join(hex_var[2])))
print('"{}" * "{}" = "{}"'.format(''.join(hex_var[0]), ''.join(hex_var[1]), ''.join(hex_var[3])))
