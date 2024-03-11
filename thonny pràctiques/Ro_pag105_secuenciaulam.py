#Ro_pag105_secuenciaulam.py

x = int(input("Indica el nombre per començar: "))

while x > 1:
    if x%2 == 0:
        x = x/2
    else:
        x = 3*x+1

print("Valor final: ",x)