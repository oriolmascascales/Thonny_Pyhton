#Ro_pag95_ex8.py

from math import *

a1 = float(input("Introdueix la 1a nota d'un estudiant = "))
a2 = float(input("Introdueix la 2n nota del mateix estudiant = "))
a3 = float(input("Introdueix la 3a nota del mateix estudiant = "))

b1 = float(input("Introdueix la 1a nota de l'altre estudiant = "))
b2 = float(input("Introdueix la 2n nota del mateix estudiant = "))
b3 = float(input("Introdueix la 3a nota del mateix estudiant = "))

if a1 == a2 and a2 == a3:
    a4 = a1 + a2
    print (a4)
elif a1 == a2:
    if a1 > a3:
        a4 = a1 + a2
        print(a4)
elif a1 == a3:
    if a1 > a2:
        a4 = a1 + a3
        print(a4)
elif a2 == a3:
    if a2 > a1:
        a4 = a2 + a3
        print(a4)
elif a2 == a3:
    if a1 > a2:
        a4 = a2 + a3
        print(a4)
elif a1 == a3:
    if a2 > a1:
        a4 = a1 + a3
        print(a4)
elif a2 == a1:
    if a3 > a2:
        a4 = a2 + a3
        print(a4)

if b1 == b2 and b2 == b3:
    b4 = b1 + b2
    print (b4)
elif b1 == b2:
    if b1 > b3:
        b4 = b1 + b2
        print(b4)
elif b1 == b3:
    if b1 > b2:
        b4 = b1 + b3
        print(b4)
elif b2 == b3:
    if b2 > b1:
        b4 = b2 + b3
        print(b4)
elif b2 == b3:
    if b1 > b2:
        b4 = b2 + b3
        print(b4)
elif b1 == b3:
    if b2 > b1:
        b4 = b1 + b3
        print(b4)
elif b2 == b1:
    if b3 > b2:
        b4 = b2 + b3
        print(b4)

if a4 < b4:
    print("El estudiant amb millor nota és el segon")

if a4 > b4:
    print("El estudiant amb millor nota és el primer")