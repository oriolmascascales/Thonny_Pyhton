#Pràctica per l'examen

x = int(input("Valor inicial de baterias  = "))
m = int(input("Introdueix el valor màxim = "))
dia = 0

while x<=m:
    x = x*2
    dia = dia+1

print("dia =",dia)