# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 10:27:51 2026

@author: ACER
"""
for i in range(9):
    print("Hello") 

for i in range(1,9):
    print(i)

for i in range(-2, 20 , 3): 
    print (i)

for i in range(10, 0 ,-3):
    print(i)

s = "Setayesh"
for i in s:
    print(i)

s = "Setayesh , Mohammad"
for i in s:
    if i=="m":
        print(i)
        
count = 0 
m = ["Setayesh", "Mohammad", "Setayesh" ]
for i in m :
    if i=="Setayesh" :
        count = count + 1
print(count)

number = [ 23 , 24 , 25 , 26 , 27 , 28 , 29 , 39]
for i in number :
    if i%2==0 :
        print(i) 