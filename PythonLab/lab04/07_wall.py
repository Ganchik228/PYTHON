#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич
st_x=0
st_y=0
width=100
height=50
RN=20
BN=10
for i in range(RN):
    sdvig = 0 if i%2==0 else 50
    for j in range(BN):
        lx = st_x + sdvig + width * j
        ly = st_y + height * i
        rx = lx + width
        ry = ly + height
        left_bottom=sd.get_point(lx,ly)
        right_top=sd.get_point(rx,ry)
        sd.rectangle(left_bottom=left_bottom,right_top=right_top,width=1)
sd.pause()
