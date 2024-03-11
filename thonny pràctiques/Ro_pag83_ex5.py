#Ro_pag83_ex5

from math import *

cantitat = int(input("Intrdueix la cantitat dipositada en dolars = "))

billet100 = cantitat // 100
billet50 = (cantitat % 100)//50
billet20 = (cantitat % 50)//20
billet10 = (cantitat % 20)//10
billet5 = (cantitat % 10)//5
billet1 = (cantitat % 5)//1

print("Els billets que equivaldrien a la cantitat inicial sera de: ")

print("billets de 100",billet100)
print("billets de 50",billet50)
print("billets de 20",billet20)
print("billets de 10",billet10)
print("billets de 5",billet5)
print("billets de 1",billet1)