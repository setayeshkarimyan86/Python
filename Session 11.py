# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 08:44:49 2026

@author: ACER
"""
file = open("test.tex","w") 
file.write("Salam") 
file.close() 

file = open("test.tex","r")
file1 = file.read()
print(file1)
file.close()

file = open("test.tex","a")
file.write("\nChetori ?")
file.close()

with open("test.tex","w") as file :
    file.write("\nKojaii ?")

name = input("Enter your name")
lastname = input("Enter your lastname")
with  open("Info.tex" , "w") as file :
    file.write(name)
    file.write("\n" + lastname) 