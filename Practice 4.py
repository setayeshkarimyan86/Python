# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 14:48:55 2026

@author: ACER
"""
def check_info(**kwargs) :
    if "name" in kwargs :
        print("vojood darad")
    else :
        print("vojood nadarad")
check_info(name = "Setayesh" , age = 19 )


def average_grade(**kwargs): 
    total = 0
    for grade in kwargs.values() :
        total += grade
    average = total / len(kwargs) 
    return average 
print(average_grade(zist = 18, riazi = 19, farsi = 18)) 


def sum(*args) :
    total = 0
    for number in args :
        total += number 
    return total 
s = sum(89 , 14 , 6 , 38)
print(s) 