#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("Реализуем алгоритм Евклида итерационным и рекурсивным способом. Если оба алгоритма работают верно, их результаты должны совпадать")
a,b=int(input("Ищем коэфициенты в формуле НОД(x,y)=ax+by. Введите первое число:  ")), int(input("Введите второе число:  "))


def gcdex_method_one(a, b):

    x, x1, y, y1 = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, x1 = x1, x - x1*q
        y, y1 = y1, y - y1*q
    return (a, x, y)


def gcdex_method_two(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcdex_method_two(b, a % b)
        return d, y, x - y * (a // b)

    
print('НОД, коэффициент a, коэффициент b в формуле НОД(x,y)=ax+by соответственно. Первый способ:', gcdex_method_one(a,b))
print('НОД, коэффициент a, коэффициент b в формуле НОД(x,y)=ax+by соответственно. Второй способ:',gcdex_method_two(a,b))



