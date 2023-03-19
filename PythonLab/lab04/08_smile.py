#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код
def smile():
    point = sd.random_point()
    sd.circle(center_position=point,radius=50)
    y1 = sd.get_point(point.x-20,point.y+10)
    y2 = sd.get_point(point.x+20,point.y+20)
    sd.circle(center_position=y1,radius=10)
    sd.circle(center_position=y2,radius=13)
    st=sd.get_point(point.x-20,point.y-20)
    end=sd.get_point(point.x+20,point.y-30)
    sd.line(start_point=st,end_point=end)

for _ in range(10):
    smile()
sd.pause()
