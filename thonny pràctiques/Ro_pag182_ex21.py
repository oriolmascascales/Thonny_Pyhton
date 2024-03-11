#Ro_pag182_ex21.py

from math import*

def suma_boles_for (n):
    t = (n*(n+1))/2
    print("n: ",t,"f(n): ",n)

a = int(input("Introdueix el valor que vols: "))

for i in range (1,a+1):
    suma_boles_for (i)

def suma_boles_while (n):
    j=0
    i=1
    while i <=n:
        j =j+i
        print("n: ",i,"f(n): ",j)
        i = i+1
