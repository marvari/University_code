#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle as tl
 
def draw_fractal_sierpinski(length,depth):  # функция принимает два параметра
    if depth==0:
        for i in range(0,3):
            tl.forward(length)
            tl.left(120)
    else:
        draw_fractal_sierpinski(length/2,depth-1)
        tl.forward(length/2)
        draw_fractal_sierpinski(length/2,depth-1)
        tl.back(length/2)
        tl.left(60)
        tl.forward(length/2)
        tl.right(60)
        draw_fractal_sierpinski(length/2,depth-1)
        tl.left(60)
        tl.back(length/2)
        tl.right(60)
 

tl.speed(100000)  # увеличиваем скорость черепашки
tl.pensize(2)
tl.penup()
tl.goto(-400, -350)  # сдвигаем начальное положение, чтобы поместился большой фрактал
tl.pendown()
tl.color('purple')
draw_fractal_sierpinski(900,6)


