# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 14:15:18 2026

@author: ACER
"""
class student() : 
    def __init__(self , name , lastname , mark) :
        self.name = name 
        self.lastname = lastname 
        self.mark = mark 
    def reportcard(self) :
        print(f"it's for {self.name} {self.lastname} and the mark in reportcard is {self.mark}")
a = input("Enter the name :")
b = input("Enter the lastname :")
c = int(input("Enter the mark :"))
std = student(a , b , c) 
std.reportcard() 


class animals() :
    def __init__(self , name , itstype) :
        self.name =name 
        self.itstype = itstype
    def introducinganimals1(self) :
        print(f"today's animal is {self.name} and it's {self.itstype} .")
class details(animals) :
    def __init__(self , color , size , name , itstype) :
        animals.__init__(self , name , itstype) 
        self.color = color
        self.size = size
    def introducinganimals2 (self) :
        print(f"{self.name} is a {self.itstype} animal.it's size is {self.size} and it's {self.color}")
dtls = details("yellow" , "big" , "lion" , "wild")
dtls.introducinganimals2() 
dtls.introducinganimals1() 