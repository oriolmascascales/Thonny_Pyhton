#Ro_areayvolum_ingemecanica.py

from math import*

def cuadrado (a):
    a = float(input("Introdueix valor a: "))
    A = a**2
    P = 4*a
    print("A: ",A, "P: ",P)
    return[A,P]
def triangle (a,b,c,h):
    a = float(input("Introdueix valor a: "))
    b = float(input("Introdueix valor b: "))
    h = float(input("Introdueix valor h: "))
    A=(b*h)/2
    P=a+b+c
    return[A,P]
    print("A: ",A, "P: ",P)
def rectangulo (a,b):
    a = float(input("Introdueix valor a: "))
    b = float(input("Introdueix valor b: "))
    A = b*a
    P = 2*(a+b)
    print("A: ",A, "P: ",P)
    return[A,P]
def paralelogram (a,b,h):
    a = float(input("Introdueix valor a: "))
    b = float(input("Introdueix valor b: "))
    h = float(input("Introdueix valor h: "))
    A = b*h
    P = 2*(b+h)
    print("A: ",A, "P: ",P)
    return[A,P]
def rombo (a,d,D):
    a = float(input("Introdueix valor a: "))
    D = float(input("Introdueix valor D: "))
    d = float(input("Introdueix valor d: "))
    A = (D*d)/2
    P = 4*a
    print("A: ",A, "P: ",P)
    return[A,P]
def cometa (a,b,d,D):
    a = float(input("Introdueix valor a: "))
    D = float(input("Introdueix valor D: "))
    d = float(input("Introdueix valor d: "))
    b = float(input("Introdueix valor b: "))
    A = (D*d)/2
    P = 2*(b+a)
    print("A: ",A, "P: ",P)
    return[A,P]
def trapezi (a,b,B,c,h):
    a = float(input("Introdueix valor a: "))
    B = float(input("Introdueix valor D: "))
    c = float(input("Introdueix valor d: "))
    b = float(input("Introdueix valor b: "))
    h = float(input("Introdueix valor h: "))
    A  = ((B+b)*h)/2
    P = B+b+a+c
    print("A: ",A, "P: ",P)
    return[A,P]
def circulo (r):
    r = float(input("Introdueix valor r: "))
    A = pi*r**2
    P = 2*pi*r
    print("A: ",A, "P: ",P)
    return[A,P]
def poligon_regular (a,b):
    a = float(input("Introdueix valor a: "))
    b = float(input("Introdueix valor b: "))
    A = (P*a)/2
    P = n*B
    print("A: ",A, "P: ",P)
    return[A,P]
def corona_circular (R,r):
    r = float(input("Introdueix valor r: "))
    R = float(input("Introdueix valor R: "))
    A = pi*(R**2 - r**2)
    print("A: ",A)
    return[A]
def sector_circular (R,n):
    R = float(input("Introdueix valor R: "))
    n = float(input("Introdueix valor n: "))
    A = (pi*R**2*n)/360
    print("A: ",A)
    return[A]
def cubo (a):
    a = float(input("Introdueix valor a: "))
    A = 6*a**2
    v = a**3
    print("A: ",A, "V: ",V)
    return[A,V]
def cilindre (R,h):
    R = float(input("Introdueix valor R: "))
    h = float(input("Introdueix valor h: "))
    A = 2*pi*R*(h+R)
    V = pi*R**2*h
    print("A: ",A, "V: ",V)
    return[A,V]
def ortoedro (a,b,c):
    a = float(input("Introdueix valor a: "))
    b = float(input("Introdueix valor b: "))
    c = float(input("Introdueix valor c: "))
    A = 2*(a*b+a*c+b*c)
    V = a*b*c
    print("A: ",A, "V: ",V)
    return[A,V]
def prisma_recte (P,h,a):
    a = float(input("Introdueix valor a: "))
    H = float(input("Introdueix valor H: "))
    A = P*(h+a)
    V = A*h
    print("A: ",A, "V: ",V)
    return[A,V]
def con (R,g,h):
    R = float(input("Introdueix valor R: "))
    g = float(input("Introdueix valor g: "))
    h = float(input("Introdueix valor h: "))
    A = pi*R*(R+g)
    V = (pi*R**2*h)/3
    print("A: ",A, "V: ",V)
    return[A,V]
def tronco_de_cono (g,r,R,h):
    g = float(input("Introdueix valor g: "))
    r = float(input("Introdueix valor r: "))
    R = float(input("Introdueix valor R: "))
    h = float(input("Introdueix valor h: "))
    A = pi*[g*(r+R)+r**2+R**2]
    V = (pi*h*(R**2+r**2+R*r)/3)
    print("A: ",A, "V: ",V)
    return[A,V]
def esfera (R):
    R = float(input("Introdueix valor R: "))
    A = 4*pi*R**2
    V = (4*pi*R**3)/3
    print("A: ",A, "V: ",V)
    return[A,V]
def pirámide (P,Ab,ab,ap):
    ab = float(input("Introdueix valor ab: "))
    Ab = float(input("Introdueix valor Ab: "))
    ap = float(input("Introdueix valor ap: "))
    A = (P*(ab+ap))/2
    V = (Ab*h)/3
    print("A: ",A, "V: ",V)
    return[A,V]
def tetraedro_regular (a):
    a = float(input("Introdueix valor a: "))
    A = sqrt(3)*a**2
    V = (sqrt(2)*a**3)/12
    print("A: ",A, "V: ",V)
    return[A,V]
def octaedro_regular (a):
    a = float(input("Introdueix valor a: "))
    A = 2*sqrt(3)*a**2
    V = (sqrt(2)*a**3)/3
    print("A: ",A, "V: ",V)
    return[A,V]
def tronco_de_pirámide (Pb1, Pb2, Ab1, Ab2,h,a):
    Pb1 = float(input("Introdueix valor Pb1: "))
    Pb2 = float(input("Introdueix valor Pb2: "))
    Ab1 = float(input("Introdueix valor Ab1: "))
    Ab2 = float(input("Introdueix valor Ab2: "))
    a = float(input("Introdueix valor a: "))
    h = float(input("Introdueix valor h: "))
    A = ((Pb1+Pb2))/2*a+Ab1+Ab2
    V = ((Ab1+Ab2+sqrt(Ab1*Ab2))*h)/3
    print("A: ",A, "V: ",V)
    return[A,V]
def casquete_esférico (R,h):
    R = float(input("Introdueix valor R: "))
    h = float(input("Introdueix valor h: "))
    A = 2*pi*R*h
    V = (pi*h**2*(3*R-h))/3
    print("A: ",A, "V: ",V)
    return[A,V]
def huso_cuña_esférica (R,n):
    R = float(input("Introdueix valor R: "))
    n = float(input("Introdueix valor n: "))
    A = (4*pi*R**2*n)/360
    V = (4*pi*R**3*n)/3*360
    print("A: ",A, "V: ",V)
    return[A,V]
def zona_ó_segmento_esférico (R,h,r1, r2):
    R = float(input("Introdueix valor R: "))
    h = float(input("Introdueix valor h: "))
    r1 = float(input("Introdueix valor r1: "))
    r2 = float(input("Introdueix valor r2: "))
    A = 2*pi*R*h
    V = (pi*h*(h**2+3*r1**2+3*r2**2))/6
    print("A: ",A, "V: ",V)
    return[A,V]
#==========================================================================

from math import pi, sqrt

def cuadrado():
    a = float(input("Introduce valor a: "))
    A = a**2
    P = 4*a
    print("A:", A, "P:", P)
    return A, P

def triangle():
    a = float(input("Introduce valor a: "))
    b = float(input("Introduce valor b: "))
    h = float(input("Introduce valor h: "))
    A = (b*h)/2
    P = a+b+h
    print("A:", A, "P:", P)
    return A, P

def rectangulo():
    a = float(input("Introduce valor a: "))
    b = float(input("Introduce valor b: "))
    A = b*a
    P = 2*(a+b)
    print("A:", A, "P:", P)
    return A, P

def paralelogram():
    a = float(input("Introduce valor a: "))
    b = float(input("Introduce valor b: "))
    h = float(input("Introduce valor h: "))
    A = b*h
    P = 2*(b+h)
    print("A:", A, "P:", P)
    return A, P

def rombo():
    a = float(input("Introduce valor a: "))
    D = float(input("Introduce valor D: "))
    d = float(input("Introduce valor d: "))
    A = (D*d)/2
    P = 4*a
    print("A:", A, "P:", P)
    return A, P

def cometa():
    a = float(input("Introduce valor a: "))
    D = float(input("Introduce valor D: "))
    d = float(input("Introduce valor d: "))
    b = float(input("Introduce valor b: "))
    A = (D*d)/2
    P = 2*(b+a)
    print("A:", A, "P:", P)
    return A, P

def trapezi():
    B = float(input("Introduce valor B: "))
    b = float(input("Introduce valor b: "))
    c = float(input("Introduce valor c: "))
    a = float(input("Introduce valor a: "))
    h = float(input("Introduce valor h: "))
    A = ((B+b)*h)/2
    P = B+b+a+c
    print("A:", A, "P:", P)
    return A, P

def circulo():
    r = float(input("Introduce valor r: "))
    A = pi*r**2
    P = 2*pi*r
    print("A:", A, "P:", P)
    return A, P

def poligon_regular():
    a = float(input("Introduce valor a: "))
    n = float(input("Introduce valor n: "))
    P = n*a
    A = (P*a)/2
    print("A:", A, "P:", P)
    return A, P

# Continúa con las demás funciones de la misma manera...

# Ejemplo de uso:
cuadrado()
triangle()
rectangulo()
paralelogram()
rombo()
cometa()
trapezi()
circulo()
poligon_regular()
