#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает ингридиентов - создать соответствующие функции в модуле my_burger

import my_burger

print("Двойной чизбургер:")
my_burger.add_bun()
my_burger.add_patty()
my_burger.add_cheese()
my_burger.add_patty()
my_burger.add_cheese()
my_burger.add_pickle()
my_burger.add_mayo()
my_burger.add_bun()

print('__________________\n')

print("Мой бургер:")
my_burger.add_bun()
my_burger.add_patty()
my_burger.add_cheese()
my_burger.add_tomato()
my_burger.add_pickle()
my_burger.add_mayo()
my_burger.add_bun()