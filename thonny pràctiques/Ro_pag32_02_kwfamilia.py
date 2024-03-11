#Ro_pag32_02_kwfamilia.py

preu = float(input("Introdueix el preu de la llum = "))
Kwh = float(input("Introdueix la llum consumida = "))

if Kwh > 700:
    preu5 = (Kwh*preu)*0.05+preu*Kwh
    print("Preu a pagar serà de = ",preu5)

if Kwh < 700:
    preunormal = Kwh*preu
    print("Preu a pagar serà de = ",preunormal)