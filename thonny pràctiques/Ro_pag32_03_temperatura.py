#Ro_pag32_03_temperatura.py

temp = float(input("Introdueix la temperatura = "))
codigo = float(input("Introdueix 1 per passar a graus celsius i 2 per a graus fahrenheit = "))

if codigo==1:
    tempc=5/9*(temp-32)
    print("temperatura amb graus celsius = ",tempc)
if codigo==2:
    tempf=32+9*temp/5
    print("temperatura amb graus fahrenheit ",tempf)