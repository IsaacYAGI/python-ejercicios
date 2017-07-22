'''
De un operario se conoce su sueldo y los años de antigüedad. Se pide
confeccionar un programa que lea los datos de entrada e informe:
a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un aumento de 5 %.
c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios.
'''

sueldo_oper = float(input("Ingrese el sueldo del operario: "))

anios_trab = int(input("Ingrese los anios de servicio del operario: "))

if sueldo_oper < 500 and anios_trab >= 10:
    print("Se aumenta el 20% del sueldo.")
    print("El nuevo sueldo es: ",sueldo_oper*0.20+sueldo_oper)
else:
    if sueldo_oper < 500 and anios_trab < 10:
        print("Se aumenta el 5% del sueldo.")
        print("El nuevo sueldo es: ",sueldo_oper*0.05+sueldo_oper)
    else:
        if sueldo_oper > 500:
            print("El sueldo se mantiene sin cambios")
            print("El sueldo actual es: ",sueldo_oper)
