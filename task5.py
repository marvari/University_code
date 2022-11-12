#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
(a, b) = (int(input("Введите числа через 'enter'")), int(input()))


def my_gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a


print ('наш нод:', my_gcd(a, b), 'библиотечный нод:', math.gcd(a, b))
