##Calcular el sueldo mensual de un operario conociendo la cantidad de horas
##trabajadas y el valor por hora.

CANT_DIAS = 30
cant_horas = int(input("Ingrese la cantidad de horas trabajadas: "))
sueldo = float(input("Ingrese el sueldo por hora del trabajador: "))

print("El sueldo mensual del trabajador es: ",cant_horas*sueldo*CANT_DIAS)
