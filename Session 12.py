# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 08:35:48 2026

@author: ACER
"""
age = 20 
if age < 20 :
    print("Yes")
if age >= 20 :
    print("No") 
if age > 20 :
    print("Old")
if age <= 20 :
    print("Young")

age = int(input("Enter your age :")) 
if age > 18 :
    print("it is allowed")
else :
    print("it isn't allowed")

grade = 20 
if grade > 10 :
    print("Pass")

if grade > 18 :
    print("Great")

grade =19
if grade > 10 : 
    print("Pass")
elif grade > 18 :
    print("Great")

number = int(input("Enter a number :")) 
if number % 2 == 0 :
    print("Even")
else :
    print("Odd") 

action = input("Enter the action:") 
if action == "Shoot" :
    print("++")
elif action == "Pas" :
    print("+")
elif action == "Goal" :
    print("+++") 