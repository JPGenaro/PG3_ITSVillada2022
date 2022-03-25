def ejercicio_3():
    print("==Ejercicio N°3==")
    width = int(input("Indique el ancho: "))
    height = int(input("Indique el lato: "))
    caracter = input("Escriba el caracter: ")

    for i in range(width):
        for j in range(height):
            print(caracter, end=" ")
        print("")

ejercicio_3()