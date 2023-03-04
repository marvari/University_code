#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def my_gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a

if __name__ == '__main__':
    
    print ('НОД:', my_gcd(a, b))

