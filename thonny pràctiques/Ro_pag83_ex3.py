#Ro_pag83_ex3

from math import *

numero_1 = int(input("introdueix un nombre de dos xifres = "))
numero_2 = int(input("introdueix un altre nombre de dos xifres = "))

xifra_central_1 = (numero_1 // 10) % 10
xifra_central_2 = (numero_2 // 10) % 10

resultat = (xifra_central_1) + (xifra_central_2)

print("El resultat de la suma dels dos nombre centrals ha sigut de = ",resultat)