#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача 6.
# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше загаданного введенное пользователем число.
# Если за 10 попыток число не отгадано, то вывести его.

import random

ATTEMPT = 10
print('Угадайте число сгенерированное компьютером от 0 до 100 за "{}" попыток!'.format(ATTEMPT))
x = random.randint(0, 100)
text = '\nВы не смогли угадать число!'
print(x)

for _ in range(0, ATTEMPT):
    var = int(input('Ваше число: '))
    if var > x:
        print('Ваше число больше!')
    elif var < x:
        print('Ваше число меньше!')
    else:
        text = '\nВы угадали число!'
        break

print(text)

