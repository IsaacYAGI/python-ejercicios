cant_preguntas = int(input("Ingrese la cantidad total de preguntas: "))

cant_correctas = int(input("Ingrese la cantidad total de preguntas respondidas correctamente: "))

porcentaje = cant_correctas*100/cant_preguntas

if porcentaje < 50:
    print("Fuera de nivel")
else:
    if porcentaje < 75:
        print("Nivel regular")
    else:
        if porcentaje < 90:
            print("Nivel medio")
        else:
            print("Nivel maximo")
