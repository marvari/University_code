#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def my_gcd(num1, num2):
    while num2 != 0:
        (num1, num2) = (num2, num1 % num2)
    return num1

import math

if __name__ == '__main__':

    (num1, num2) = (int(input()), int(input()))
    print (my_gcd(num1, num2))
    
