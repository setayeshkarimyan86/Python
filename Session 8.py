# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 17:19:11 2026

@author: ACER
"""
personal = { "name" : ["Setayesh" , "Maedeh" , 86 , 85 ] , "lastname" : "Karimyan" , "age" : 18}
print(personal["name"].index(85))
print(personal["name"][2] ,personal["name"][0])
personal["age"] = 19
personal["city"] = "ShahreBabak"
print(personal)
print(personal.keys())
print(personal.values())
print(personal.items())
print(len(personal))
print(personal.get("name"))
print(personal.get("name",-1))

s = input("Enter name")
t = input("Enter age")
information = { "name1" : s , "age1" : t}
print(information)  