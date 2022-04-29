numero_1 = int(input("Ingrese un numero: "))
numero_2 = int(input("Ingrese otro numero: "))

try:
    resultado = numero_1 / numero_2
except ZeroDivisionError:
    print("No se puede dividir entre 0")
except:
    print("Error desconocido")
else:
    print("El resultado es: ", resultado)

