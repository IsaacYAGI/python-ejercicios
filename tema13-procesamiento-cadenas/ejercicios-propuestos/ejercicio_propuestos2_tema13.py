'''
Ingresar una oración que pueden tener letras tanto en mayúsculas como
minúsculas. Contar la cantidad de vocales.
Crear un segundo string con toda la oración en minúsculas para que
sea más fácil disponer la condición que verifica que es una vocal.
'''

cadena = input("Ingrese una oracion: ")

cadena_min = cadena.lower()

vocales = "aeiou"

long_cad = len(cadena)

cant_voc = 0

for i in range(0,long_cad):
    #Buscamos si el caracter actual esta en la cadena de vocales
    if cadena_min[i] in vocales:
        #De existir, se suma uno al contador
        cant_voc += 1

print("La oracion ingresada es: ",cadena)
print("La cantidad de vocales: ",cant_voc)
