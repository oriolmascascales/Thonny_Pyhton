#Ro_pag44_exercici3.py

a = int(input("Introdueix un nombre a = "))
b = int(input("Introdueix un nombre b = "))
c = int(input("Introdueix un nombre c = "))

r = 0

while not a<b and c<=0:
    if b % 2 == 0:
        b = b-1
    else:
        r = r+c
        b = b-1

print ("El nombre r = ",r)