n = int(input("Quantitat de valors: "))
v = []
for i in range(n):
    x = int(input("Inserta la seguent dada: "))
    v = v+[x]

s = 0

for e in v:
    if e%2==0:
        s=s+e
print("La suma dels valors es: ",s)