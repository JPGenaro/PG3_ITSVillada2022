
resultado = 0
try:
    numero_1 = int(input("Ingrese un numero: ")) 
    numero_2 = int(input("Ingrese otro numero: "))
    resultado = numero_1 + numero_2
except ValueError:
    print("Oopss... Lo que ha ingreso no es un numero, por favor pruebe de nuevo")
except:
    print("Ha salido un error, pruebe de nuevo por favor...")

print("Suma: ", (resultado))

while True:
    consulta = str(input("¿Quiere seguir sumando valores? (Si/No)\n"))
    if consulta == "Si" or consulta == "SI" or consulta == "si":
        numero_3 = int(input("Ingrese el numero: "))
        resultado += numero_3
        print("Suma: ", (resultado))
    elif consulta == "No" or consulta == "NO" or consulta == "no":
        print("Goodbye...")
        break