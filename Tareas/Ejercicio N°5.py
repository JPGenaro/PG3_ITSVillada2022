def ejercicio_5():
    print("==Ejercicio N°5==")
    texto: str = input("Ingrese la palabra: ")
    if str(texto) == str(texto)[::-1]:
        print(f"{texto} = True")
    else:
        print(f"{texto} = False")

ejercicio_5()