'''
Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe
cuántos tienen notas mayores o iguales a 7 y cuántos menores.
'''

notas_mayores = 0
notas_menores = 0
i = 1

while i <=10:
   # nota_act = float(input("Ingrese nota "+str(i)+": "))
    nota_act = float(input(f"Ingrese nota {i}: "))
    if nota_act >= 7:
        notas_mayores += 1
    else:
        notas_menores += 1

    i += 1

print("La cantidad de estudiantes con notas mayores a 7 es de: ",notas_mayores)
print("La cantidad de estudiantes con notas menores a 7 es de: ",notas_menores)
