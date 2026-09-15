# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 18:19:34 2026

@author: ACER
"""
for i in range(6): 
    for j in range(6):
        print(i * j , end=" ")
    print()

    
for i in range(1,10,2):
    print(i)


f = []
for i in range(1,10,2):
    f.append(i)
print(f)


a = "fatemeh"
for i in range(len(a)):
    print(i)


a = ["fatemeh","zahar"] 
b = ["afzali"]
c = [17]
for i in zip(a,b,c):
    print(i) 



a = ["fatemeh"] 
b = [17]
c = dict(zip(a,b))
print(c)



from random import randint 
print(randint(1, 10))


javab = randint(1,6)
a = int(input(" عدد را وارد کنید "))
if javab == a:
    print("your found")
    
else:
    print(f"javab in bood {javab}") 