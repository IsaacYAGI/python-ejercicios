'''
Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se
ingresaron. Tener en cuenta que un espacio en blanco es igual a " ",
en cambio una cadena vacía es ""
'''

cadena = input("Ingrese una oracion: ")

long_cad = len(cadena)

espaces = 0

for i in range(0,long_cad):
    if (cadena[i] == " "):
        espaces += 1
    
print("La oracion ingresada es: ",cadena)
print("La cantidad de espacios en blanco es: ",espaces)
