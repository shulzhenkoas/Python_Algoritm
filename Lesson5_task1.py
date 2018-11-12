# __author__ = 'Шульженко А.С.'
# Coding: UTF-8

# Задача 1.
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
# наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.

from collections import namedtuple
from collections import defaultdict


def profit(num):
    mass_company = defaultdict(lambda: 'Предприятие не найдено!')  # Для будущего функционала
    company = namedtuple('company', 'one_section two_section three_section four_section annual')

    for _ in range(num):
        logotype = input('\nВведите название компаниии:')
        spam = []
        for i in range(4):
            spam.append(float(input('Введите прибыль за ' + str(i + 1) + ' квартал: ')))
        spam.append(sum(spam))
        mass_company[logotype] = company(*spam)

    avrg = 0
    for key in mass_company.keys():
        avrg += mass_company[key].annual
    avrg = avrg / len(mass_company)

    spam = [key for key in mass_company.keys() if mass_company[key].annual > avrg]
    print('\nПредприятия, чья прибыль выше средней годовой - "{}":'.format(avrg))
    print(*spam, sep='\n')
    spam = [key for key in mass_company.keys() if mass_company[key].annual < avrg]
    print('\nПредприятия, чья прибыль ниже средней годовой - "{}":'.format(avrg))
    print(*spam, sep='\n')

profit(int(input('Введите количество предприятий:')))
