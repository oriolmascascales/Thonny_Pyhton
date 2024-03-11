#Ro_pag95_ex1

from math import *

r = float(input("Introdueix de radi = "))
h = float(input("Introdueix de altura = "))
pi = 3.1415

if h>r:
    v = 3.1415 * pow(r,2) * h
    print("Volumen = ",v)

else:
    a = 2*pi*r*h + 2*pi*pow(r,2)
    print("àrea = ",a)