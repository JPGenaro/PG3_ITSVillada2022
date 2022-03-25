def ejercicio_6():
    print("__Ejercicio N°6==")
    palabra = str(input("Ingrese una palabra: "))
    contador = 0
    for letra in palabra:
        if letra.lower() in "aeiouAEIOU":
            contador += 1
    print(contador)

ejercicio_6()