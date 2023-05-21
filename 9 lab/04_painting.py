#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать (или при необходимости написать) функции отрисовки
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

import simple_draw as sd
import draw_library as dl

screen_width = 1400
screen_height = 1000
sd.resolution = (screen_width, screen_height)

sun_center = sd.get_point(70, screen_height - 70)
sun_radius = 70
sd.circle(sun_center, sun_radius, color=sd.COLOR_YELLOW, width=0)

rb_center = sd.get_point(500, -250)
rb_start_radius = 1100
rb_line_width = 18

dl.draw_rainbow(dl.rainbow_colors, rb_center, rb_start_radius, rb_line_width)

brick_width, brick_height = 40, 20
wall_width, wall_height = 600, 400
start_wall_x, start_wall_y = 100, 80
wall_color = (255, 140, 0)

dl.draw_wall(wall_width, wall_height, brick_width, brick_height, start_wall_x, start_wall_y, wall_color)

win_height = 160
win_width = 122
win_color = (240, 230, 140)
win_left_bottom = sd.get_point(wall_width/2 - win_width/2 + start_wall_x, wall_height/2 - win_height/4 + start_wall_y)
win_right_top = sd.get_point(wall_width/2 + win_width/2 + start_wall_x, wall_height/2 + win_height*3/4 + start_wall_y)

dl.draw_window(win_left_bottom, win_right_top, win_color)
roof_top = sd.get_point(start_wall_x + wall_width / 2, start_wall_y + wall_height + 120)
roof_left = sd.get_point(start_wall_x, start_wall_y + wall_height)
roof_right = sd.get_point(start_wall_x + wall_width, start_wall_y + wall_height)
sd.polygon([roof_left, roof_top, roof_right], color=(255, 0, 0), width=0)

dl.draw_smile(int(wall_width/2 + start_wall_x * 2)-40, int(wall_height/2 - start_wall_y) + 250, sd.COLOR_DARK_GREEN)

root_point = sd.get_point(1100, 290)
dl.draw_branches(root_point, 90, 45)

root_point = sd.get_point(750, 30)
dl.draw_branches(root_point, 90, 80)

snowflake_color = sd.COLOR_WHITE
for i in range(30):
    x = sd.random_number(start_wall_x + wall_width, screen_width)
    y = sd.random_number(0, screen_height)
    size = sd.random_number(10, 40)
    sd.snowflake(center=sd.get_point(x, y), length=size, color=snowflake_color, factor_a=0.3, factor_b=0.6, factor_c=60)

drift_color = (220, 220, 220)
drift_x = start_wall_x + wall_width + 50
drift_y = start_wall_y - 20
sd.rectangle(sd.get_point(drift_x, drift_y), sd.get_point(drift_x + 200, drift_y + 70), color=drift_color, width=0)
sd.rectangle(sd.get_point(drift_x + 30, drift_y + 70), sd.get_point(drift_x + 170, drift_y + 120), color=drift_color, width=0)
sd.rectangle(sd.get_point(drift_x + 70, drift_y + 120), sd.get_point(drift_x + 130, drift_y + 170), drift_color, width=0)

sd.pause()

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.