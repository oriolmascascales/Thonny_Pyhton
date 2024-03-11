#equció 2n grau

a = int(input("Indica la lletra a: "))
b = int(input("Indica la lletra b: "))
c = int(input("Indica la lletra c: "))

if b**2-4*a*c < 0:
    print("Solució imaginària")

x = (b**2)-4*a*c

o1 = (-b + sqrt(x))/(2*a)
o2 = (-b - sqrt(x))/(2*a)

print ("La solució positiva és: ",o1)
print ("La solució negativa és: ",o2)