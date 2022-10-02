#!/usr/bin/python
# -*- coding: utf-8 -*-

import math  # Подключение модуля "math"
import numpy  # Подключение модуля "numpy"
import matplotlib.pyplot as mpp  # Подключение модуля "matplotlib", для данного модуля задается сокращение "mpp"

# Эта программа рисует график функции, заданной выражением ниже

if __name__ == '__main__':  # Проверка на то, запущен ли файл напрямую
    arguments = numpy.arange(0, 200, 0.1)  # Задаем значения по оси ОХ из данного диапазона с конкретным интервалом
    mpp.plot(arguments, [math.sin(a) * math.sin(a / 20.0) for a in
             arguments])  # Значения на оси OY получаются по следующей формуле
    mpp.show()  # Вывод графика
