# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 08:53:44 2026

@author: ACER
"""
l = [1 , 2, 3]
for a in l :
    pass
 
for a in [1 , 2, 3] :
    if a==3 :
        break
    print(a) 

c = [ "ali" , "mohamad" , "sara" , "raha"] 
for a in c :
        if a == "sara" :
            print("sara is found")
            break  

for i in [1 , 2, 3, 4]:
    if i== 3 :
        continue 
    print(i) 


m = [1 , 2, 3 ,4 , 5]
n = []
for i in m :
    n.append(i)
    print(n)
print("\n",n) 

n = [1 , 2 ,3 , 4, 5, 6 , 7, 8 , 9, 10]
odd = []
for i in n :
    if i%2 == 0 :
        odd.append(i)
print(odd) 

o = [ 1,2,3,4,5]
p = [ a*2 for a in o ]
h = [a%2==0 for a in o] 
print(p)
print(h) 

r = [1 , 2 , 3 , 4 , 5 , 6]
t = [a for a in r if a%2==0 ]
print(t) 