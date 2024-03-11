#Ro_pag71_ex4.py

from math import *

t = float(input("Introdueix el temps en anys = "))

k = (50-(2*exp(0.1*10)))/10

crecimiento = k*t + 2*pow(e,0.1*t)

print(crecimiento)