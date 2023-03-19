#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код
# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
# TODO здесь ваш код
def bubble(point,step,color):
    radius=50
    for _ in range(3):
        radius+=step
        sd.circle(center_position=point,radius=radius,color=color)

#point = sd.get_point(100,100)
#bubble(point,10,(255,0,0))

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

#for y in range(100,400,100):
#    for x in range(100,1100,100):
#        point = sd.get_point(x,y)
#        bubble(point,10,(228,133,7))

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
for _ in range(100):
    point=sd.random_point()
    color=sd.random_color()
    bubble(point,5,color)
sd.pause()
