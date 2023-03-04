#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math


print ('Привет! Я программа начиающего питониста и пока умею только проверять на простоту числа(1) и считать НОД целых чисел(2). Введи цифру в скобках, и увидишь что я могу.')
q = int(input())

if q == 1:

    from module1 import Wilsons_theorem
    
    print ('Осуществим проверку нашего числа с помощью теоремы Вильсона.')
    a = int(input('Введите число, которое вы хотите проверить '))

    print (Wilsons_theorem(a))
    
elif q == 2:

    from module2 import my_gcd
    
    (a, b) = (int(input("Введите первое число ")), int(input("Введите второе число ")))

    print (my_gcd(a,b))


