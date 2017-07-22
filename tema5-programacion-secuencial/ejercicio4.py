##Realizar la carga del precio de un producto y la cantidad a llevar.
##Mostrar cuanto se debe pagar (se ingresa un valor entero en el precio del producto)

cant_prod = int(input("Ingrese la cantidad del producto: "))
precio_prod = int(input("Ingrese el precio del producto: "))

print("La cantidad a pagar por ",cant_prod, " producto(s) a un precio de ",precio_prod," es de ", cant_prod*precio_prod)
