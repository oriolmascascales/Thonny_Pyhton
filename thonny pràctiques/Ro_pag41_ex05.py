#Ro_pag41_ex5.py

def calcular_suma_serie(n):
    suma = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            suma += i
        else:
            suma += i ** 2
    return suma

x = int(input("Ingresa el valor de x: "))

terminos = 0
suma_acumulada = 0

while suma_acumulada <= x:
    terminos += 1
    if terminos % 2 == 1:
        suma_acumulada += terminos
    else:
        suma_acumulada += terminos ** 2


print(f"La cantidad de términos que deben sumarse para que la suma sea mayor que {x} es: {terminos}")
