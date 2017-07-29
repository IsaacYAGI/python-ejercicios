'''
Confeccionar una programa con las siguientes funciones:
1) Generar una lista con 5 elementos enteros aleatorios comprendidos entre 1 y 3.
2) Controlar que el primer elemento de la lista sea un 1, en el caso que haya un 2 o 3 mezclar la lista y volver a controlar hasta que haya un 1. 
3) Imprimir la lista.
'''

import random


def llenar_arreglo(li):
    for i in range(5):
        li.append(random.randint(1,3))

def arreglo_tiene_uno(li):
    for i in range (len(li)):
        if (li[i] == 1):
            return True
    return False

def arreglo_tiene_uno_primero(li):
    return li[0] == 1

def vaciar_arreglo(li):
    del(li[0:])

def mezclar(li):
    random.shuffle(li)

lista = []

array_valido = False

while not array_valido:
    llenar_arreglo(lista)
    print("La lista generada es: ",lista)
    if (arreglo_tiene_uno(lista)):
        if (arreglo_tiene_uno_primero(lista)):
            print("Lista validada, lista: ",lista)
            array_valido = True
        else:
            while (not arreglo_tiene_uno_primero(lista)):
                print("La lista ",lista," no tiene 1 primero.")
                mezclar(lista)
            print("Lista validada, lista: ",lista)
            array_valido = True
    else:
        vaciar_arreglo(lista)
        print("Vaciando lista")
        
