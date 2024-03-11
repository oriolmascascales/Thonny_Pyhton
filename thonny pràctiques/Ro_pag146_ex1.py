#Ro_pag141_ex1.py

from math import *

n = int(input("Ingrese la cantidad de paquetes: "))

suma_pesos = 0
pesos = []

for i in range(n):
    peso = float(input(f"Ingrese el peso del paquete (i+1): "))
    pesos.append(peso)
    suma_pesos += peso

promedio = suma_pesos / n
minimo = min(pesos)
maximo = max(pesos)

print(f"El promedio de los pesos es: (promedio)")
print(f"El peso mínimo es: (minimo)")
print(f"El peso máximo es: (maximo)")
