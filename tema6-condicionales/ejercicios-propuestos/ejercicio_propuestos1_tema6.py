##Realizar un programa que solicite la carga por teclado de dos números,
##si el primero es mayor al segundo informar su suma y diferencia,
##en caso contrario informar el producto y la división
##del primero respecto al segundo.

num1 = int(input("Ingrese el numero 1: "))
num2 = int(input("Ingrese el numero 2: "))

if (num1 > num2):
    print("La suma de ",num1," y ",num2," es de ", num1+num2)
    print("La diferencia de ",num1," y ",num2," es de ", num1-num2)
else:
    print("El producto de ",num1," y ",num2," es de ", num1*num2)
    print("La division de ",num1," y ",num2," es de ", num1/num2)
