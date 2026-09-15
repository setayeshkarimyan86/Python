# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 10:03:53 2026

@author: ACER
"""
a = ("Ali" , 20 , "Kerman")
name , age , city =a
print(name)
print(age)
print(city)

my_tuple = (1 , 2 , 3, "Setayesh")
for i in my_tuple :
    print(i) 
    
person = (("S" , 19) , ("M" , 22))
for name , age in person :
    print(f"{name} is {age} years old")
 
s = {"Ali" : (14 , 150) , "Mohammad" : (22 , 175)}
for i in s :
    print( i , s[i])
    print(i) 

info = { "Setayesh" : (19 , 159 , "Kerman") , "Mohammad" : (22 , 175 ," Kerman") } 
for k,v in info.items() :
    print(k,v) 
 
while True :
    print("Hello World")
    
a = 0
while a <= 5 :
    print(a)
    a+=1  