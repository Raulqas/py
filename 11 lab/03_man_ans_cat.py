# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint


class House:

    def __init__(self):
        self.food = 50
        self.cat_food = 0
        self.money = 150
        self.dirt = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, кошачьей еды осталось {}, грязи {}'.format(
            self.food, self.money, self.cat_food, self.dirt)


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def adopt_cat(self, cat):
        cat.house = self.house
        cprint('{} подобрал кота'.format(self.name), color='cyan')

    def buy_cat_food(self):
        if self.house.money >= 50:
            cprint('{} купил кошачью еду'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cat_food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def clean_house(self):
        cprint('{} убрался в доме'.format(self.name), color='blue')
        self.house.dirt -= 100
        self.fullness -= 20

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        if self.fullness < 40:
            self.eat()
        elif self.house.food < 50 or self.house.cat_food < 30:
            if self.house.money >= 50:
                dice = randint(1, 2)
                if dice == 1:
                    self.shopping()
                else:
                    self.buy_cat_food()
            else:
                self.work()
        elif self.house.dirt > 100:
            self.clean_house()
        elif self.house.money < 300:
            self.work()
        else:
            self.watch_MTV()


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Кот - {}, сытость {}'.format(self.name, self.fullness)

    def sleep(self):
        cprint('Кот {} спал'.format(self.name), color='green')
        self.fullness -= 10

    def eat(self):
        if self.house.cat_food >= 10:
            cprint('Кот {} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            cprint('Коту {} нет еды'.format(self.name), color='red')

    def tear_wallpapers(self):
        cprint('Кот {} драл обои'.format(self.name), color='magenta')
        self.fullness -= 10
        self.house.dirt += 5

    def act(self):
        if self.fullness <= 0:
            cprint('Кот {} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.tear_wallpapers()
        else:
            self.eat()


citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни'),
]

cats = [
    Cat(name='Гарфилд'),
    Cat(name='Том'),
]

my_sweet_home = House()
for citizen in citizens:
    citizen.go_to_the_house(house=my_sweet_home)

citizens[0].adopt_cat(cats[0])
citizens[1].adopt_cat(cats[1])

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citizen in citizens:
        citizen.act()
    for cat in cats:
        cat.act()
    my_sweet_home.food = min(my_sweet_home.food, 200)
    my_sweet_home.cat_food = min(my_sweet_home.cat_food, 200)
    my_sweet_home.dirt = max(my_sweet_home.dirt, 0)
    print('--- в конце дня ---')
    for citizen in citizens:
        print(citizen)
    for cat in cats:
        print(cat)
    print(my_sweet_home)
