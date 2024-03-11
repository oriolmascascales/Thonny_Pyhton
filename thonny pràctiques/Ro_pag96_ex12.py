#Ro_pag96_ex12.py

from math import *

cantidad = int(input("Introdueix el nombre de productes = "))
precio = float(input("Introdueix el cost del productes = "))

if cantidad == 1 or cantidad < 5:
    cost1 = precio*cantidad
    print("El preu sera = ",cost1)

elif cantidad == 5 or cantidad < 10:
    cost2 = (precio*0.95)*cantidad
    print("El preu sera = ",cost2)

elif cantidad ==  10 or cantidad > 10:
    cost3 = (precio*0.92)*cantidad
    print("El preu sera =  ",cost3)