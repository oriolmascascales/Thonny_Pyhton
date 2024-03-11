#Ro_pag148_dado_ganancias

from random import*

x = int(input("Introdueix el nombre d'intents: "))
d = 0

n = randint(1,6)

for i in range (1,x+1):
    if n == 1:
        d = d+1
    elif n == 6:
        d = d+5
    elif n == 2 or n == 3 or n == 3 or n == 5:
        d = d-2

if d>0:
    print("Has guanyat ",d)
if d<0:
    print("Has perdut ",d)