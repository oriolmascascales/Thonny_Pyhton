#Ro_challenge17-10-2023.py

a = int(input("Introdueix el nombre a = "))
b = int(input("Introdueix el nombre b = "))
c = int(input("Introdueix el nombre c = "))
d = int(input("Introdueix el nombre d = "))

if (a>0) or (b>a) and (not c == d):
    a = c
    b = 0
else:
        c = (d+c)
        if c == 0:
            c = (c+b)
        else:
                 c = (c-a)
        b = (a+c+d)

print ("Llavors els valors a,b,c,d, son = ",a,b,c,d)