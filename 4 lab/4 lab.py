#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
# TODO здесь ваш код
mounth = 10
result = 0
while mounth > 0:
    pc = (expenses/100)*3
    result += (expenses - educational_grant)
    expenses += pc
    mounth -= 1
print('Студенту надо попросить', round(result,2), 'Рублей')

# TODO здесь ваш код
