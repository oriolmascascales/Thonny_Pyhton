#Ro_pag81_ex1

from math import *

r = int(input("Introdueix el radi del cilindre = "))
a = int(input("Introdueix la altura del cilindre = "))
pi = 3.141592

area = 2*pi*r*a + 2*pi*r**2
volum = pi*r**2

print ("Area del cilindre = ",area)
print ("Volum del cilindre = ",volum)