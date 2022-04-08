#Ejercicio de desafio de python (Triangulo)
def ejercicio_desafio():
    altura: int = int(input("Altura del triángulo: "))
    caracter: str = str(input("Ingrese el caracter: "))

    for i in range(1, altura+1):
        #Espacio entre cada caracter
        for j in range(altura - i):
            print("   ", end="")
        #Creacion del triangulo
        for j in range(1, 2 * i):
            print(f" {caracter} ", end="")
        print()

def ejercicio_desafio_2():
    altura: int = int(input("Altura del triángulo: "))
    caracter: str = str(input("Ingrese el caracter: "))

    for i in range(altura):
        #Espacio entre cada caracter
        for j in range(0, i):
            print(" ", end="")
        #Creacion del triangulo
        for j in range(i, altura):
            print(f" {caracter}", end="")
        print()

    ejercicio_desafio()

ejercicio_desafio()
ejercicio_desafio_2()