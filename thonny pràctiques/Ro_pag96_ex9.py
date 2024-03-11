#Ro_pag95_ex9.py

from math import *

n1 = float(input("Introdueix una nota = "))
n2 = float(input("Introdueix una nota = "))
n3 = float(input("Introdueix una nota = "))

if n1 == n2 and n2 == n3:
    print("La nota més alta i baixa són =",n1)
elif n1 < n2 and n2 < n3:
    print("La nota més alta és =",n1)
    print("La nota més baixa és =",n3)
elif n1 > n2 and n2 > n3:
    print("La nota més alta és =",n3)
    print("La nota més baixa és =",n1)
elif n2 > n1 and n1 > n3:
    print("La nota més alta és =",n2)
    print("La nota més baixa és =",n3)
elif n3 > n2 and n2 < n1:
    print("La nota més alta és =",n3)
    print("La nota més baixa és =",n2)
    