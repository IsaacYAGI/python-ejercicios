#Confeccionar un programa que permita cargar un número entero positivo
#de hasta tres cifras y muestre un mensaje indicando si tiene 1, 2, o 3 cifras.
#Mostrar un mensaje de error si el número de cifras es mayor.

num = int(input("Ingrese el numero: "))

if num < 10:
    print("El numero tiene una cifra")
else:
    if num < 100:
        print("El numero tiene dos cifras")
    else:
        if num < 1000:
            print("El numero tiene tres cifras")
        else:
            print("Error, el numero tiene mas de tres cifras")
