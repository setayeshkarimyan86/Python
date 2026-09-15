# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 09:08:17 2026

@author: ACER
"""
class calculater () :
    def __init__(self , num1 , num2) :
        self.num1 = num1
        self.num2 = num2 
    def plus(self) : 
        print(self.num1 + self.num2) 
    def zarb(self) :
        print(self.num1 * self.num2) 
calc = calculater(2 , 6)
calc.plus()
calc.zarb()


class circle () :  
    pi = 3.14
    def __init__(self , r):
        self.r = r
    def primeter(self) : 
        p = self.r * self.r * self.pi
        return p
a = int(input("Enter shoae :"))
s = circle(a) 
print( s.primeter() ) 


class newbook() : 
    def __init__(self , name , page) :
        self.name = name 
        self.page = page
    def open(self) :
        print(f"{self.name} is watch {self.page}")
pages = newbook("riazi" , 98) 
pages.open()
class darsi(newbook) : 
    def __init__(self , reshteh , sal , name , page): 
        newbook.__init__(self, name, page) 
        self.reshteh = reshteh 
        self.sal =sal
    def payan(self) : 
        print(f"I am {self.reshteh} and {self.sal} and I am reading {self.page} of {self.name} book")
d = darsi("tajrobi" , 11 , "zist" , 78)
d.payan() 
d.open() 
print(d.page , d.name) 
print(pages.name , pages.page)
print(type(pages)) 
print(type(d)) 