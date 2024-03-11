

n = int(input("Introdueix quantes vegades vols que es divideixi = "))
denominador = 1
pi = 0
x = 0

for i in range(n = n+1):
    if i/2 == 0:
       denominador = denominador *(-1)
    else:
        denominador = denominador *(+1)
    pi=(1/denominador)-(1/denominador+2)
    pi = pi/4
print("pi = ",pi)