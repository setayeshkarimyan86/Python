# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 10:14:52 2026

@author: ACER
"""
class runner() :
    def __init__(self , name) :
        self.name = name
    def action(self) :
        print(f"{self.name} is running")
class football():
    def __init__(self , name) :
        self.name = name
    def action(self):
        print(f"{self.name} is a player") 
r = runner("Ali")
f = football("Mohammad")
r.action()
f.action()
print(type(r))
print(type(f)) 


from tqdm import tqdm 
from time import sleep
for i in tqdm(range(1000)) :
    sleep(0.1) 
    

import emoji 
s = emoji.emojize("Setayesh is :red_heart:")
print(s)


import numpy as np
m = [ 23 , 89 , 61 , 50]
print(np.median(m))