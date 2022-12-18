#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import math
from typeguard import typechecked


print('Осуществим проверку нашего числа с помощью теоремы Вильсона.')
a= random.randrange(-100000, 100000)


@typechecked
def Wilsons_theorem(a:int) ->int: #По теореме Вильсона: число простое, если (a-1)!+1 делится на a
    flag=True
    if a>=0:
        if (math.factorial(a - 1) + 1) % a != 0:  
            flag= False
    else:
        if (math.factorial((-1) * a - 1 ) + 1 ) % ((-1) * a)!= 0:  # Тут пришлось  чуть-чуть схитрить, ведь факториал определен для натурального числа
            flag= False
    return(flag)
        

print('Теорема Вильсона:', a, Wilsons_theorem(a))


try:
     print(Wilsons_theorem(0,5))
     print('Теорема Вильсона:', a, Wilsons_theorem(a))
except:
    print('float, ой, это не целое положительное число')

try:
    print(Wilsons_theorem(-10))
    print('Теорема Вильсона:', a, Wilsons_theorem(a))
except:
    print('int, ой, это не целое положительное число')


