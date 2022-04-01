# Ejercicio 1
from lib2to3.pygram import pattern_symbols


def ejercicio_1():
    print("==Ejercicio N°1==")
    lista: list[int]= [1, 25, 43, 94, 55, 16, 7, 78, 39]
    print(f"Lista: {lista}")
    buscador = int(input("Ingrese un numero: "))
    def buscar(lista, buscador):
        try:
            print(lista.index(buscador))
        except:
            print("El numero ingresado no esta en la lista o no es un numero...")

    buscar(lista, buscador)

ejercicio_1()