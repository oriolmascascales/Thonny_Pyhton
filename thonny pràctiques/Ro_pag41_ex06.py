#Ro_pag41_ex6.py

total_granos_requeridos = 0

suma_parcial = 0

for i in range(1, 65):
    granos_casilla = 2 ** (i - 1)
    suma_parcial += granos_casilla
    total_granos_requeridos += granos_casilla

total_toneladas_requeridas = total_granos_requeridos / (1_000_000)

print(f"La cantidad total de granos de trigo requeridos es: {total_granos_requeridos} granos")
print(f"La cantidad total de toneladas de trigo requeridas es: {total_toneladas_requeridas} toneladas")
