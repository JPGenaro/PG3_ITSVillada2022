# Ejercicio 2
def ejercicio_2():
    print("==Ejercicio N°2==")
    time: int = int(input("Escriba el año: "))
    if not time % 4 and (time % 100 or not time % 400):
        print("Es bisiesto")
    else:
        print("No es bisiesto")

ejercicio_2()