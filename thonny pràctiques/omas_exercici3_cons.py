#cons

c = int(input("Introdueix el número de conos que utilitzras: "))
m = int(input("Introdueix la distància en que els vols en metres: "))
dis = 0

if c == 1 or c == 0:
    print("Coloca el cono allà on desitjis")

elif c < 1:
    dis = m / c
    dis = dis/100
print("Hauras de posar els conos a ",dis,"cm de distància")