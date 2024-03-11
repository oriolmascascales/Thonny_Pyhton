#Ro_pag97_ex18.py

from math import *

p = float(input("Introdueix el pes en kg = "))
t = float(input("Introdueix la altura en metres = "))

imc = p/(pow(t,2))

if imc < 20:
    print("Estado desnutrido")

elif imc == 20 and imc < 25:
    print("Estado normal")

elif imc == 25 and imc < 30:
    print("Estado sobrepeso")

elif imc == 30 and imc < 35:
    print("Estado obesidad grado 1")

elif imc == 35 and imc < 40:
    print("Estado obesidad grado 2")

elif imc < 40:
    print("Estado obesidad grado 3")