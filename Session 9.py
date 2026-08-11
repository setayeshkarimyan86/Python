# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 10:03:54 2026

@author: ACER
"""
s = {6 , 3 , 9, "Sara","Maedeh", "Seatyesh"}
s.add("Ali")            #Add Element
s.update([7,"h"])       #Add Elements
print(s) 
print( 3 in s)          #Check if element exist in a set 
print("Ali" not in s)   #Check membership
m = {2 , 4 , 6 , 10}
n = {1 , 3 , 5 , 10}
print(m.union(n))         #Union of tow sets
print(m.intersection(n))  #The intersection of two sets

m = {1 ,2 , 3}
n = {2 , 4 , 6}
o = m.intersection(n)     #The intersection of two sets
print(o)
s ={6 , "Dina" , 6 , 9}   #Duplicate Element
print(s) 

a = {6 , 9 , 12 , 15 }
b = {3 , 6 , 9 , 12 , 15 , 18}
result = a.issubset(b)
print(result)
a.remove(9)              #Remove an element
print(a)
a.clear()               #Clear a set
print(a)
a.discard(18)          #
print(a) 

python = {"Setayesh" , "Maryam" , "Ali" , "Elham" , "Neda" , "Pooya" }
web = { "Maryam" , "Elham" ,"Pooya"}
bothclass = python.intersection(web) 
classes = python.union(web)
print(bothclass)
print(classes)
 