# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 08:37:07 2026

@author: ACER
"""
a = True 
b = "True"
print(type(a))
print(type(b))

c  = 20
print(c == 20)

s = "Ali"
print(s=="ali")
print(s=="Ali")

mydic = {"name" : "Setayesh" , "lastname" :"Karimyan" , "age" : 19 }
print("name" in mydic) 

mylist = [ 1 , 20 ,"S"]
print(1 in mylist)
print("S" not in mylist)

age = int(input("Enter your age ="))
city = input("Enter your city =")
print( age <= 40 and city == "Tehran")
print( age <= 40 or city == "Tehran") 

h = "12"
print(h.isdigit()) 
k = "1.2"
print(k.isdigit())

print(bool({}))
print(bool({90}))
print(bool(" "))
print(bool(""))

number = int(input("Enter the Number ="))
print(number % 2 == 0)

student = True
print(not student)

sen = int(input("Enter your age ="))
print(not sen) 