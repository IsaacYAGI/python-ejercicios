##Se ingresa por teclado un número positivo de uno o dos dígitos (1..99)
##mostrar un mensaje indicando si el número tiene uno o dos dígitos.
##(Tener en cuenta que condición debe cumplirse para tener dos dígitos
##un número entero)

num = int(input("Ingrese un numero entero de uno o dos digitos: "))

if (num < 10):
    print("El numero ",num," tiene un digito")
else:
    print("El numero ",num," tiene dos digitos")

