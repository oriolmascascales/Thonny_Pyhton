#Ro_pag32_01_areavolumradicilindre.py

radi = float(input("Introdueix el radi del cilindre = "))
altura = float(input("introdueix el altura del cilindre = "))

if altura > radi:
    volum=3.1416*radi**2*altura
    print("Volum = ",volum)

area = (2*3.1416*radi*altura)+(2*3.1416*radi**2)
print("Area del cilindre = ",area)