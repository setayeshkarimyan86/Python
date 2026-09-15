# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 10:07:28 2026

@author: ACER
"""
def student(*nomres , **info) : 
    total = 0 
    for nomre in nomres :
        total += nomre
        avg = total / len(nomres) 
        print("name:",info.get("name"))
        print("age:" , info.get("age")) 
        print("average:", avg) 
student(18,20,15 , name = "ali" , age = 18 ) 


a = [1 , 2,  3, 4]
print(*a) 


def tavan2(a) : 
    return a**2 
my_list=[2,4,6]
tavan = map(tavan2, my_list) 
print(tavan) 
print(list(tavan)) 


my_list = [2 , 4, 6]
tavan = map(lambda x : x**2 , my_list)
print(list(tavan)) 



my_list = ["2" , "4" , "6"]
a = map( int , my_list) 
print(a)
print(list(a)) 


z = [1 , 4 , 3 , 8 , 18 , 15] 
even = filter(lambda c : c%2==0 , z)
print(list(even)) 


s = [ 2.8 , 9 , 3.7 , 5.4 , 770 , 188] 
print( list(filter(lambda d : d != int(d), s))) 


w = [ 2 , 3, 8 , 9 , 4 , 6]
even = filter(lambda t : t%2==0 , w) 
tavn2 = map(lambda i : i**2 , even)
print(list(tavn2)) 