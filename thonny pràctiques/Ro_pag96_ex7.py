#Ro_pag95_ex6.py

from math import *

a = float(input("Introdueix la temperatura = "))
b = int(input("Marca 1 si esta en farenheit i 2 per celsius  = "))

if b == 1:
    c = 3/5*(a-32)
    print("La temperatura en celius és = ",c)

elif b == 2:
    d = 32+9*a/5
    print("La temperatura en farenheit és = ",d)