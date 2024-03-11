#omas_1.py
from math import*

def y_f_a (a):
    y = 4 + sin (a)
    print ("y = ",y, "alfa = ",a)

def y_f_b (b):
    y = 4 + 230 * sin (b)
    print("y = ",y,"aplfa = ",b)

c = int(input("Introdueix el valor que vols: "))
z = int(input("Indica amb un 0 si vols fer servir la funció y=4+sin(a), o amb un 1 si vols fer servir la funció de y=4+230*sin(a). : "))

for i in range (45, 360+1):
    if z == 0:
        y_f_a (i)
    else z == 1:
        y_f_b (i)
    else z not == 0 or not == 1:
        print("torna a indicar amb un 0 si vols fer servir la funció y=4+sin(a), o amb un 1 si vols fer servir la funció de y=4+230*sin(a). : ")