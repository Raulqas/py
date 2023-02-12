#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.


stol_quantity  = store[goods['Стол']][0]['quantity']
stol_quantity1 = store[goods['Стол']][1]['quantity']
stol_price = store[goods['Стол']][0]['price']
stol_price1 = store[goods['Стол']][1]['price']
stol_cost = stol_quantity * stol_price + stol_quantity1 * stol_price1
print('Стол -', stol_quantity+stol_quantity1, 'шт, стоимость', stol_cost, 'руб')



div_quantity  = store[goods['Диван']][0]['quantity']
div_quantity1 = store[goods['Диван']][1]['quantity']
div_price = store[goods['Диван']][0]['price']
div_price1 = store[goods['Диван']][1]['price']
div_cost = div_quantity * div_price + div_quantity1 * div_price1
print('Диван -', div_quantity+div_quantity1, 'шт, стоимость', div_cost, 'руб')


stul_quantity  = store[goods['Стул']][0]['quantity']
stul_quantity1 = store[goods['Стул']][1]['quantity']
stul_quantity2 = store[goods['Стул']][2]['quantity']
stul_price = store[goods['Стул']][0]['price']
stul_price1 = store[goods['Стул']][1]['price']
stul_price2 = store[goods['Стул']][2]['price']
stul_cost = stul_quantity * stul_price + stul_quantity1 * stul_price1 + stul_quantity2 * stul_price2
print('Стул -', stul_quantity+stul_quantity1+stul_quantity2, 'шт, стоимость', stul_cost, 'руб')
