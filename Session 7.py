# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:10:41 2026

@author: ACER
"""
mylist = [9,"t",0]
mylist.append("f")
print(mylist)
mylist.insert(1, "Setayesh")
print(mylist)
mylist[0] = "Sara"
print(mylist)
name = "Setayesh,sara,90"
myname = list(name.split(","))
print(myname)
s = ["d", "h" ]
t = " ".join(s)
print(t)
m = ('hossein',80,'setayesh',90)
print(m)
print(type(m))

t = ("kerman","sirjan","anar","tehran")
s = list(t)
print(t[0],t[3])
print(s)
print("kerman" in t , 6 in t)
