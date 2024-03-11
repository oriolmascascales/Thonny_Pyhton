#Ro_pag95_ex6.py

from math import *

p = float(input("Introdueix els Kw consumits = "))

if p > 700:
    a = p % 700
    b = a * 0.5
    c = a + b
    print ("Preu = ",c)

elif p <= 700:
    d = 700 * 0.07
    print ("Preu = ",d)