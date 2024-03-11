#Ro_pag_180_ex1.py

def conteo (n):
    c = 0
    for i in range(1,n+1):
        if n % i == 0:
            c = c+1
            print("nº",c,"divisor",i)
    print("Té un toto de: ",c, " divisors")

a = 0
b = 0
f = 1
for a in range (1, 101):
    if a % f == 0:
        b = b+1
        print("nº",b,"divisor",f)
        f = f+1
    print("Té un toto de: ",b, " divisors")