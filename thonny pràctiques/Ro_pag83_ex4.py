#Ro_pag83_ex4

from math import *

numero_1 = int(input("introdueix un nombre de dos xifres = "))

xifra_central = (numero_1 // 100)
xifra_primera = (numero_1 % 100) // 10
xifra_ultima = (numero_1 % 10)

numero_nou = (xifra_ultima*100) + (xifra_primera*10) + (xifra_central*1)

print("El resultat és = ",numero_nou)

#la xifre_primera i la xifra_central estan nomenats al revés