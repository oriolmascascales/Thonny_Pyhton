#Ro_pag41_ex4.py

def calcular_aproximacion_pi(n):
    aproximacion_pi = 0
    signo = 1
    divisor = 1

    for i in range(n):
        termino = 1 / divisor * signo
        aproximacion_pi += termino
        divisor += 2
        signo = -signo

    return aproximacion_pi * 4

n = int(input("Ingresa la cantidad de términos para calcular pi: "))

aproximacion = calcular_aproximacion_pi(n)

print(f"La aproximación de pi con {n} términos es: {aproximacion}")
