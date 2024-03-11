#Ro_pag147_ex22_juegoranas.py

from random import*

x1=0
y1=0
x2=0
y2=0
x3=0
y3=0
i1=0
i2=0
i3=0

while not x1==20:
    d=randint(1,4)
    i1=i1+1
    if d==1:
        x1=x1+1
    elif d==2:
        x1=x1-1
    elif d==3:
        y1=y1+1
    elif d==4:
        y1=y1-1
print("Quantitat d'intents granota 1: ",i1)

while not x2==20:
    d=randint(1,4)
    i2=i2+1
    if d==1:
        x2=x2+1
    elif d==2:
        x2=x2-1
    elif d==3:
        y2=y2+1
    elif d==4:
        y2=y2-1
print("Quantitat d'intents granota 2: ",i2)

while not x3==20:
    d=randint(1,4)
    i3=i3+1
    if d==1:
        x3=x3+1
    elif d==2:
        x3=x3-1
    elif d==3:
        y3=y3+1
    elif d==4:
        y3=y3-1
print("Quantitat d'intents granota 3: ",i2)

if i1 < i2 and i1 < i3:
    print("GUANYADORA GRANOTA 1")
elif i2 < i1 and i2 < i3:
    print("GUANYADORA GRANOTA 2")
elif i3 < i2 and i3 < i1:
    print("GUANYADORA GRANOTA 3")