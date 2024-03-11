#Ro_pag81_ex8.py

from math import *

p = int(input("Aportacions econòmiques de cada més = "))
a = valor_acomulat
n = int(input("Número d'aportacions = "))
x = tasa_interés_mensual

valor_acomulat = p(((1+x)**n)-1/x)
print(a)