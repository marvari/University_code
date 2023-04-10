#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from multiprocessing import Pool


def my_func(x):
    # функция f(x) = - x^2 + 1
    return - (x ** 2) + 1


def my_func_int(a, b):
    # Определенный интеграл по формуле Ньютона-Лейбница для f(x)
    return - ((b ** 3) / 3) + b - ( - ((a ** 3) / 3) + a)
  

def mc_integrate(res):
    func, a, b, n = res
    # Интегрируем от a до b
 
    vals = np.random.uniform(a, b, n)
    y = [func(val) for val in vals]

    y_mean = np.sum(y) / n
    integ = (b - a) * y_mean
   
    return integ


if __name__ == '__main__':
    with Pool(4) as pool:
        res = (pool.map(mc_integrate,[(my_func, 0, 1, 500000),(my_func, 0, 1, 500000),(my_func, 0, 1, 500000), (my_func, 0, 1, 500000)]))
    print(f"Монте-Карло: {mc_integrate([my_func, 0, 1, 500000]): .4f}")
    print("Монте-Карло уточненный:", sum(res)/len(res))
    print(f"Аналитика: {my_func_int(0, 1): .4f}")
