'''
En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500,
realizar un programa que lea los sueldos que cobra cada empleado e informe
cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300.
Además el programa deberá informar el importe que gasta la empresa en sueldos
al personal.
'''

cant_empl = int(input("Ingrese la cantidad de empleados: "))

importe_total = 0
i = 1
cant_may_300 = 0

while i <= cant_empl:
    sueldo = float(input(f"Ingrese sueldo de trabajador #{i}: "))
    if (sueldo > 300):
        cant_may_300 += 1
        
    importe_total += sueldo
    i += 1

print("La cantidad de empleados que ganan mas de 300$ es de: ",cant_may_300)
print("La cantidad de empleados que ganan menos de 300$ es de: ",cant_empl - cant_may_300)
print("El importe total de la empresa es: ",importe_total)
