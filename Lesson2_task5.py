#__author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача 5.
# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.

START_ASCII = 32
END_ASCII = 127
text = ''
pair = 0

for i in range(START_ASCII, END_ASCII + 1):
    text += '"{}":"{}"'.format(i, chr(i))
    pair += 1
    if pair == 10:
        text += '\n'
        pair = 0
    else:
        text += '\t'

print('Таблица ASCII символов от "{}" до "{}":\n{}'.format(START_ASCII, END_ASCII, text))
