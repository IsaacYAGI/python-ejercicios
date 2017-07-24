'''
Realizar la carga de dos nombres de personas distintos.
Mostrar por pantalla luego ordenados en forma alfabética.
'''

nombre1 = input("Ingrese el primer nombre: ")

nombre2 = input("Ingrese el segundo nombre: ")

if nombre1 > nombre2:
    print("El orden es: ",nombre2,", ",nombre1)
else:
    print("El orden es: ",nombre1,", ",nombre2)
