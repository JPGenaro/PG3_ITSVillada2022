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
    
ejercicio_desafio()