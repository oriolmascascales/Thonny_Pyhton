#Ro_pag148_ex27.py

n = int(input("Ingresa una dada: "))
r = 0

while n>0:
    d = n%2
    n = n//2
    r = 10*r+d
    print(d, r, n)