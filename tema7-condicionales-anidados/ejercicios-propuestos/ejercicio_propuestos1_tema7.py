#Se cargan por teclado tres números distintos.
#Mostrar por pantalla el mayor de ellos.

num1 = int(input("Ingrese el num 1: "))
num2 = int(input("Ingrese el num 2: "))
num3 = int(input("Ingrese el num 3: "))

mayor = 0

if num1 > mayor:
    mayor = num1

if num2 > mayor:
    mayor = num2

if num3 > mayor:
    mayor = num3

print("El numero mayor de los tres numeros ingresados es: ",mayor)
