#Ro_pag96_ex11.py

from math import *

p1x = float(input("Introdueix el punt 1 x = "))
p1y = float(input("Introdueix el punt 1 y = "))
p2x = float(input("Introdueix el punt 2 x = "))
p2y = float(input("Introdueix el punt 2 y = "))

distancia1 = sqrt(pow(p1x,2)+pow(p1y,2))
distancia2 = sqrt(pow(p2x,2)+pow(p2y,2))

if distancia1 < distancia2:
    print("Distancia més petita és el punt 2")

elif distancia2 < distancia1:
    print("Distancia més petita és el punt 1")

elif distancia1 == distancia2:
    print("Tenen les mateixes distancies")