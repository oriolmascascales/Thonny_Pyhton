#Ro_pag104_sumaquadrat.py

n = int(input("Digues el nombre on vols que s'arribi: "))

i = 1
s = 0

while i <= n:
    c = i**2
    s = s+c
    i = i+1

print("La suma és: ",s)