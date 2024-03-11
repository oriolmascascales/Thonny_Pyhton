#Ro_pag95_ex4.py

from math import *

a = int(input("introdueix un nombre de dos xifres = "))
x = a // 10
y = a % 10

if (x+y) % 2 == 0:
    print("parell")
elif (x+y) % 2 == 1:
    print("imparell")