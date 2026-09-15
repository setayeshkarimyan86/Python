# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 10:10:26 2026

@author: ACER
"""
def add(*args) : 
    total = 0
    for number in args :
        total += number
    return total
x = add(10,20,30)
print(x) 
 

def zarb(*args) : 
    print(f"args is :{args}")
    total = 1 
    for number in args :
        total *= number 
    return total 
z = zarb(7 , 2 , 6 , 15)
print(z) 

     
def person(**kwargs) : 
    print(f"kwargs is : {kwargs}") 
    for k,v in kwargs.items() :
        print(k,v) 
print(person(name = "Setayesh" , lastname = "Karimyan"))
d = person(name = "Setayesh" , lastname = "Karimyan") 
print(d) 



def masahat(**kwargs):
    print(f"kwargs is : {kwargs}") 
    if "tool" in kwargs :
        return kwargs["tool"] * kwargs["arz"]
    if "shoae" in kwargs :
        return kwargs["shoae"] * 3.14 * kwargs["shoae"] 
print(masahat(tool = 8 , arz = 5 ))
print(masahat(shoae = 6)) 


def both(*args , **kwargs) :
    print(args) 
    print(kwargs) 
both(10 , 20 , 50 , name = "Setayesh")


a = lambda h : h%2==0 
print(a(78)) 


sum = lambda m , n : m + n 
print(sum(21 , 7)) 