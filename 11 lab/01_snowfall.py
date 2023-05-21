# -*- coding: utf-8 -*-

import random
import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку

class Snowflake:

    # TODO здесь ваш код

    def __init__(self):
        self.x = random.randint(0, sd.resolution[0])
        self.y = random.randint(0, sd.resolution[1])
        self.length = random.randint(10, 40)
        self.factor_a = random.uniform(0.1, 0.9)
        self.factor_b = random.uniform(0.1, 0.5)
        self.factor_c = random.randint(1, 30)

    def clear_previous_picture(self):
        sd.start_drawing()
        self.draw(color=sd.background_color)
        sd.finish_drawing()

    def move(self):
        self.x += sd.random_number(-10, 10)
        self.y -= self.length
        if self.x > sd.resolution[0] + 50 or self.y < -50:
            self.__init__()

    def draw(self, color=sd.COLOR_WHITE):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, color=color,
                     factor_a=self.factor_a, factor_b=self.factor_b, factor_c=self.factor_c)

    def can_fall(self):
        return self.y > -50

flake = Snowflake()

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

flakes = [Snowflake() for i in range(20)]

while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = len([flake for flake in flakes if not flake.can_fall()])
    if fallen_flakes:
        flakes.extend([Snowflake() for i in range(fallen_flakes)])
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
