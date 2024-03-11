#Ro_pag41_e3.py

n = input("Introdueix el valor de n = ")
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def suma_fibonacci(n):
    suma = 0
    for i in range(n):
        suma += fibonacci(i)
    return suma

resultat = suma_fibonacci(n)

print ("el resultat de la suma de fibonacci és = ",resultat)