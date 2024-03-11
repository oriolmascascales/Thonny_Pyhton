#omas_3.py

print("Producte 1: Gelat d'avellana:    	2,25 €")
print("Producte 2: Pastis d'atmetlla:   	1,75 €")
print()
v = int(input("Indica quin productes desitja comprar (1 o 2): "))
print()
if v != 1 or v !=2:

    print()
    print("¡Torna a indicar quin prodte vols amb un 1 o un 2!")
    print()
    
print("Només es pot pagar amb monedes de 2€, 1€, 50cèntims, 20cèntims o 5cèntims")
print()
print("Com vols pagar?")

dos = int(input("Indica amb quantes monedes de 2 € vols pagar: "))
un = int(input("Indica amb quantes monedes de 1 € vols pagar: "))
cinquanta = int(input("Indica amb quantes monedes de 0,50 € vols pagar: "))
vint = int(input("Indica amb quantes monedes de 0,20 € vols pagar: "))
cinc = int(input("Indica amb quantes monedes de 0,05 € vols pagar: "))

dos = dos*200
un = un*100
cinquanta = cinquanta*50
vint = vint*20
cinc = cinc*5

suma_pagament = dos+un+cinquanta+vint+cinc

p_1 = 225
p_2 = 175

if v == 1:
    if suma_pagament > p_1:
        t_1 = suma_pagament-p_1
        t_1 = t_1 / 100
        print()
        print("A tornar: ",t_1, "€")
    elif suma_pagament < p_1:
        f1 = suma_pagament-p_1
        f1 = f1 / 100
        print()
        print("Falten ",f1,"€ per poder adquirir el producte")
    elif suma_pagament == p_1:
        print()
        print("Has adquirit el producte 1, gelat d'avellana")

if v == 2:
    if suma_pagament > p_2:
        t_2 = suma_pagament-p_2
        t_2 = t_2 / 100
        print()
        print("A tornar: ",t_2, "€")
    elif suma_pagament < p_2:
        f2 = suma_pagament-p_2
        f2 = f2 / 100
        print()
        print("Falten ",f2,"€ per poder adquirir el producte")
    elif suma_pagament == p_2:
        print()
        print("Has adquirit el producte 2, pastis d'atmetlla")

print()
print("Gràcies per la teva compra!")