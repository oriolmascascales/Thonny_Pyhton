#Ro_pag41_e2.py

n = int(input("Introdueix el nomre de persones que votaran = "))

vot_en_contra = 0
vot_a_favor = 0

for i in range (n):
    vot = int(input("introdueix 1 per vot a favor, introdueix 0 per vot en contra = "))
    if vot == 1:
        vot_a_favor += 1
    elif vot == 0:
        vot_en_contra += 1

print ("Els resultats han sigut vots a favor = ",vot_a_favor, "i vots en contra = ",vot_en_contra)

if vot_a_favor > vot_en_contra:
    print  ("Ha guanyat vots a favor")
elif vot_en_contra > vot_a_favor:
    print ("Ha guanyat vots en contra")