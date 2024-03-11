#Ro_pag32_04_diagonals.py

base = float(input("Introdueix la base del rectangle = "))
altura = float(input("Introdueix la altura del rectangle = "))
llargada = float(input("Inntrodueix la llargaria del rectangle ="))

diagonal_1 = (llargada**2+base**2)**0.5
diagonal_2 = (base**2+altura**2)**0.5
diagonal_3 = (llargada**2+altura**2)**0.5

mayor_diagonal = max(diagonal_1,diagonal_2,diagonal_3)

print("La diagonal més gran és = ",mayor_diagonal)