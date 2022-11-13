#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
(a, b) = (int(input("Ищем НОД двух чисел двумя  способами: с помощью библиотеки math и собственной функции. Введите первое число ")), int(input("Введите второе число ")))


def my_gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a


print ('наш нод:', my_gcd(a, b), 'библиотечный нод:', math.gcd(a, b))
