#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math


def Wilsons_theorem(a): #Проверим по теореме Вильсона: число простое, если (a-1)!+1 делится на a
    flag=True
    if (math.factorial(a - 1) + 1) % a != 0:
        flag= False
    return(flag)
        
if __name__ == '__main__':

    print('Теорема Вильсона:', Wilsons_theorem(a), sep='\n')
 
