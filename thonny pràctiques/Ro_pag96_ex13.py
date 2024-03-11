#Ro_pag96_ex13.py

from math import *

horasjuan = float(input("Introdeuix les hores que ha treballat Juan = "))
salariojuan = float(input("Introdeuix el salari setmanal de Juan = "))
descuentosjuan = float(input("Introdeuix els descomptes de Juan = "))

horaspedro = float(input("Introdeuix les hores que ha treballat pedro = "))
salariopedro = float(input("Introdeuix el salari setmanal de pedro = "))
descuentospedro = float(input("Introdeuix els descomptes de pedro = "))

horasjosé = float(input("Introdeuix les hores que ha treballat José = "))
salariojosé = float(input("Introdeuix el salari setmanal de José = "))
descuentosjosé = float(input("Introdeuix els descomptes de José = "))

salario_juan = salariojuan * horasjuan - descuentosjuan

salario_pedro = salariopedro * horaspedro - descuentospedro

salario_josé = salariojosé * horasjosé - descuentosjosé

if salario_juan > salario_pedro and salario_juan > salario_pedro:
    print("El salario más grande és de Juan")

if salario_pedro > salario_juan and salario_pedro > salario_josé:
    print("El salario más grande és de pedro")
    
if salario_josé > salario_pedro and salario_josé > salario_juan:
    print("El salario más grande és de José")