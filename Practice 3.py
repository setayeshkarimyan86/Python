# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:27:37 2026

@author: ACER
"""
def sum_list(numbers) :
    total = 0
    for i in numbers :
        total += i
        return total 
def miangin_list(numbers):
    return sum(numbers) / len(numbers) 
print(miangin_list([9 , 6 , 4 , 54])) 


price = float(input ( "Enter the price :") )
discount = float(input("Enter the discount:"))
def discount_amount(price , discount) :
    return price * discount / 100
def discount_percent(price , discount_amount) :
    return discount_amount / price *100
amount = discount_amount(price , discount)
print(discount_percent(price , amount)) 