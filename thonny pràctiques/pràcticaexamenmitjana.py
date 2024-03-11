#Pràctica de for (x) in range

n = int(input("Cantidad de datos: "))
s = 0

for i in range(n):
    x=float(input("Insereix la seguent dada: "))
    s = s+x
p=s/n
print("La mitjana és: ",p)