#Ro_pag95_ex2

from math import *

r = float(input("Introdueix de radi = "))
h = float(input("Introdueix de altura = "))
pi = 3.1415

if h>r:
    v = 3.1415 * pow(r,2) * h
    print("Volumen = ",v)

else:
    print("ERROR")