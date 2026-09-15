# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 17:10:57 2026

@author: ACER
"""
def fall_n_time(name , n = 1) :
    for i in range(n) :
        return name
print(fall_n_time("Setayesh" , 2))


def sum_of_two(n1 , n2 = 10):
    return n1 + n2
print(sum_of_two(2, 9))


def is_even(n) :
    return n%2==0 
def number_even(numbers) :
    count = 0
    for n in(numbers):
        if is_even(n) :
            count +=1 
    return count
c = number_even([46 , 98 , 67 , 54])
print(c) 



def is_even(n):
    return n%2==0
def any_even_in_list(numbers) :
    for n in (numbers) :
        if is_even(n) :
            return True 
    return False 
x  = any_even_in_list([9 , 7 , 6 , 19]) 
print(x) 



def is_even(n) :
    return n%2==0 
def get_odd(numbers) :
    odd = []
    count = 0
    for i in(numbers) :
        if not is_even(i) :
            odd.append(i) 
            count+=1 
    return odd , count 
s = get_odd([34 , 23 , 76 , 19 , 86]) 
print(s) 