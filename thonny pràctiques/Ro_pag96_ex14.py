#Ro_pag96_ex14.py

from math import *

base = float(input("base = "))
altura = float(input("altura ="))

diametro  = float(input("diametro = "))

a = base*altura

if a > diametro:
    print("No passara")

elif a < diametro:
    print("Passara")

elif a == diametro:
    print("No passara")