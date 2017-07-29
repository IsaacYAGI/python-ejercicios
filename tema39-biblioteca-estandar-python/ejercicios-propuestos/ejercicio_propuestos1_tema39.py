'''
Confeccionar un programa que genere un número aleatorio entre 1 y 100 y no se muestre.
El operador debe tratar de adivinar el número ingresado.
Cada vez que ingrese un número mostrar un mensaje "Gano" si es igual al generado o "El número aleatorio el mayor" o "El número aleatorio es menor".
Mostrar cuando gana el jugador cuantos intentos necesitó.
'''
import random

def generar_numero_aleatorio():
    return random.randint(1,100)

def es_el_numero(resp_usuario,resp_correc):
    return resp_usuario == resp_correc

def numero_dado_es_mayor(resp_usuario,resp_correc):
    return resp_usuario > resp_correc

def juego_terminado(numero_correcto,numero_intentos):
    print("El juego ha terminado!")
    print("El numero correcto era",numero_correcto,"y lo resolviste en",numero_intentos,"intentos.",sep=" ")

def el_numero_es_mayor():
    print("El numero que diste es mayor al correcto, intenta de nuevo!")


def el_numero_es_menor():
    print("El numero que diste es menor al correcto, intenta de nuevo!")

def iniciar_juego():
    gano = False
    
    intentos = 1

    numero = 0

    respuesta_correc = generar_numero_aleatorio()
    
    while (not gano):
        numero = int(input("Ingresa un numero: "))
        if (es_el_numero(numero,respuesta_correc)):
            juego_terminado(respuesta_correc,intentos)
            gano = True
        else:
            if (numero_dado_es_mayor(numero,respuesta_correc)):
                el_numero_es_mayor()
            else:
                el_numero_es_menor()
            
            intentos += 1




iniciar_juego()


