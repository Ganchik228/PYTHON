#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.
step = 0
#for color in rainbow_colors:
#    start_point = sd.get_point(50+step, 50)
#    end_point = sd.get_point(550+step, 550)
#    sd.line(start_point=start_point, end_point=end_point, color=color, width=4)
#    step += 10
#sd.pause()

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код
for color in rainbow_colors:
    radius=500
    point=sd.get_point(300,-100+step)
    step+=10
    sd.circle(center_position=point,radius=radius,color=color,width=10)

sd.pause()
