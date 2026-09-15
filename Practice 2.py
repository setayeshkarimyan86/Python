# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 21:01:33 2026

@author: ACER
"""
a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
c = input("Enter operator :")
def calculation_n_time(a , b ,c) :
    if c == "+" :
        return a+b 
    elif c == "-" :
        return a-b 
    elif c == "*" :
        return a*b
    elif c == "/" :
        return a/b 
    elif c =="**" :
        return a**b 
    else :
        print("Invalid") 
s = calculation_n_time(a, b, c) 
print(s) 