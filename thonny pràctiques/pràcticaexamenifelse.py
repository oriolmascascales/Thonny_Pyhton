#Pràctica pel l'examen

a = int(input("Introdueix una calificació = "))
b = int(input("Introdueix una calificació = "))
c = int(input("Introdueix una calificació = "))

if a >= b and b >= c:
    f1 = a+b
    print("nota final = ",f1)
    
else:
    if b >= c and c>= a:
        f2 = b+c
        print("nota final = ",f2) 
    else:
        if a >= b and c >= b:
            f3 = a+c
            print("nota final = ",f3)