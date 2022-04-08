def ejercicio_3():
    print("==Ejercicio N°3==")
    width: int = int(input("Indique el ancho: "))
    height: int = int(input("Indique el lato: "))
    caracter: str = input("Escriba el caracter: ")

    for i in range(width):
        for j in range(height):
            print(caracter, end=" ")
        print("")

ejercicio_3()