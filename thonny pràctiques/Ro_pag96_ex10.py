#Ro_pag96_ex10.py

from math import *

a = float(input("Introdueix un costat a del triangle = "))
b = float(input("Introdueix un costat b del triangle = "))
c = float(input("Introdueix un costat c del triangle = "))

if a == b and a == c:
    print ("EQUILATER")
elif a == b or a == c or b == c:
    print ("ISOSCELES")
else:
    print ("ESCLALE")
