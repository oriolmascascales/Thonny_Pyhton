#Ro_exercici_02.py

n1 = float(input("Introdueix un número = "))
n2 = float(input("Introdueix un número = "))
n3 = float(input("introdueix un número = "))

if n1 > n2:
    if n1 > n3:
        print("El nombre més gran és = ",n1)

if n2 > n3:
    if n2 > n1:
        print("El nombre més gran és = ",n2)

if n3 > n1:
    if n3 > n2:
        print("El nombre més gran és = ",n3)