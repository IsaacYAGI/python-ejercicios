##Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete
##mostrar un mensaje "Promocionado".

nota1 = int(input("Ingrese la nota 1: "))
nota2 = int(input("Ingrese la nota 2: "))
nota3 = int(input("Ingrese la nota 3: "))

if (((nota1+nota2+nota3)/3) >= 7):
    print("Promocionado!")
