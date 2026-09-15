# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 17:01:43 2026

@author: ACER
"""
def hello() :
    '''
    Returns
    -------
    None.

    '''
    print("Hello World") 
hello() 

def setayesh():
    '''
    Returns
    -------
    None.

    '''
    print("1405")
setayesh() 

def hello1(name,lastname) :
    print(f"Hello World {name} {lastname}")
hello1("Setayesh","Karimyan") 

def hello2_n_time(name , n): 
    for i in range(n) :
        print(f"Hello World {name}")
hello2_n_time("Mohammad", 5) 

def numbers_n_time(a,b):
    res = a + b
    print(res) 
a = int(input("Enter the number :"))
b = int(input("Enter the number :"))
numbers_n_time(a , b) 

tool = int(input("Enter tool:"))
arz = int(input("Enter arz:"))
def masahat_n_time(tool , arz): 
    return(tool*arz) 
x = masahat_n_time(tool, arz)
print(x) 

number = int(input("Enter the number:")) 
def check_n_time(number) :
    if number %2==0 :
        return "Even"
    else :
        return "Odd"
x = check_n_time(number)
print(x)  