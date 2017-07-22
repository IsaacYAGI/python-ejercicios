##Realizar un programa que solicite ingresar
##dos números distintos y muestre por pantalla el mayor de ellos.

num1 = int(input("Ingrese el numero 1: "))
num2 = int(input("Ingrese el numero 2: "))

print("Los numero ingresados fueron: num1: ", num1," y num2 es: ",num2)

if num1>num2:
    print("El numero mayor es: ",num1)
else:
    print("El numero mayor es: ",num2)
