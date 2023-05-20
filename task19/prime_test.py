#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def is_prime(num):
    flag=True
    if (num%10)%2==0: #Проверяем четное ли число
        flag = False # Заводим сигнальную метку
    else:
        for i in range(3, int((num**0.5))+1,2): #Проверяем число на делимость. Ищем делители среди нечетных чисел в диапазоне от 3 до целой части квадратного корня из числа плюс единичка
            if num%i==0:
                flag = False
                break
    return(flag)
     
if __name__ == '__main__':

    num=int(input())
    
    print(is_prime(num))
    
    
