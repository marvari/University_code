#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Fib:
    
    class Fib_iter:
        
        def __init__(self):
            self.first = 1  # первое число
            self.second = 1  # второе число
            self.other = 0  # третье и дальнейшее число
            
        def __next__(self):
            self.other=self.first+self.second
            self.first=self.second
            self.second=self.other
            return self.other
        
    def __iter__(self):
        return Fib.Fib_iter()

        
f = Fib()
for i in f:
    print(i)

