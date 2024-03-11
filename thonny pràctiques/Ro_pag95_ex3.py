#Ro_pag95_ex2

from math import *

ax = float(input("Introdueix la base = "))
ay = float(input("Introdueix la altura = "))
bx = float(input("Introdueis la base = "))
by = float(input("Introdueix la altura = "))
cx = float(input("Introdueis la base = "))
cy = float(input("Introdueix la altura = "))

diagonal_a = sqrt(pow(ax,2)*pow(ay,2))
diagonal_b = sqrt(pow(bx,2)*pow(by,2))
diagonal_c = sqrt(pow(cx,2)*pow(cy,2))

if diagonal_a == diagonal_b and diagonal_b == diagonal_c:
    print ("Totes les diagonals són iguals")
elif diagonal_a == diagonal_b:
    if diagonal_a > diagonal_c:
        print("les diagonals més grans són a i b",diagonal_a,diagonal_b)
elif diagonal_a == diagonal_c:
    if diagonal_a > diagonal_b:
        print("les diagonals més grans són a i c",diagonal_a,diagonal_c)
elif diagonal_b == diagonal_c:
    if diagonal_b > diagonal_a:
        princt("les diagonals més grans són b i c",diagonal_b,diagonal_c)
elif diagonal_b == diagonal_c:
    if diagonal_a > diagonal_b:
        print("La diagonal més gran és a",a)
elif diagonal_a == diagonal_c:
    if diagonal_b > diagonal_a:
        print("La diagonal més gran és b",b)
elif diagonal_b == diagonal_a:
    if diagonal_c > diagonal_b:
        print("La diagonal més gran és c",c)