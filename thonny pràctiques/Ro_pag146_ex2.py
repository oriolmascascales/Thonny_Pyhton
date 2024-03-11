#Ro_pag146_ex2.py

n = float(input("Nombre de paquets: "))

x = 0
a = 0
b = 0
c = 0

while not n == x:
    pes = int(input("Pes del paquet: "))
    x = x+1
    if pes <= 10:
        a = a+1
    elif pes > 10 and pes <= 20:
        b = b+1
    else:
        c = c+1

print("Paquets de menys de 10 kg: ",a)
print("Paquets d'entre 10 kg i 20 kg: ",b)
print("Paquets de més de 20 kg: ",c)    