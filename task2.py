#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import matplotlib.pyplot as plt
import numpy as np

ITERATIONS = 20


def my_exp(x):
    """
    Вычисление экспоненты при помощи частичного суммирования
    ряда Тейлора для окрестности 0
    """

    summ = 0  # задаем переменную,отвечающую за сумму ряда
    for i in range(ITERATIONS):
        summ += x ** i / math.factorial(i)  # в цикле считаем значение каждого члена ряда и прибавляем к предыдущим значениям
    return summ


vs = np.vectorize(my_exp)
print (my_exp, vs)

help(math.exp)
help(my_exp)

print(math.exp(0.4))
print(my_exp(0.4))

angles = np.r_[-16:16:0.1]
plt.plot(angles, np.exp(angles), linewidth=1.0, color='red',
         label='библиотечная экспонента')  # делаем график
plt.plot(angles, vs(angles), linewidth=1.0, color='blue',
         label='наша экспонента')
plt.legend()
plt.show()
