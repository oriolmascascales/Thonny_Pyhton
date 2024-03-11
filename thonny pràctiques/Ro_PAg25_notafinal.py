#RO_Pag25_05_notes.py

examen = float(input("Nota del'examen sobre 100 = "))
leccion = float(input("Lliçó = "))
tarea_1 = float(input("Tasca 1 = "))
tarea_2 = float(input("Tasca 2 = "))
tarea_3 = float(input("Tasca 3 = "))

leccion = leccion*10
tarea_1 = tarea_1*10
tarea_2 = tarea_2*10
tarea_3 = tarea_3*10

nota_final = (examen*0.7) + (leccion*0.2) + (((tarea_1+tarea_2+tarea_3)/3)*0.1)

print ("Nota final",nota_final)