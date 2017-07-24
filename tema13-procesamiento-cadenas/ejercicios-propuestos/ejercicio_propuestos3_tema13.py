'''
Solicitar el ingreso de una clave por teclado y almacenarla en una cadena
de caracteres. Controlar que el string ingresado tenga entre 10 y 20
caracteres para que sea válido, en caso contrario mostrar un mensaje de error.
'''

correcto = False

while not correcto:
    password = input("Ingrese contraseña: ")

    if len(password) < 10 or len(password) > 20:
        print("Error, la contraseña debe tener minimo 10 caracteres y un maximo de 20 caracteres")
    else:
        correcto = True

print("Contraseña ",password," aceptada.")
        
