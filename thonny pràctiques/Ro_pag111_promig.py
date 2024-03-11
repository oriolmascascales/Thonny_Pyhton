#Ro_pag111_promig.py

n = int(input("Introdueix la cantitat de valors: "))

s = 0

for i in range(n):
    x = float(input("Indica la seguent dada: "))
    s=s+x
p=s/n
print("El promig és: ",p)