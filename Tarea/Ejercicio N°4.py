def ejercicio_4():
    print("==Ejercicio N°4==")
    lista: list[int] = [4, 5, 7 , 1, 5, 9, 15, 80, 42]
    print(f"Lista sin ordenar: {lista}")

    def ordenar(lista: list[int]):
        for i in range(len(lista)):
            for j in range(i+1, len(lista)):
                if lista[i] < lista[j]:
                    lista[j], lista[i] = lista[i], lista[j]

        print(lista)

    ordenar(lista)

ejercicio_4()