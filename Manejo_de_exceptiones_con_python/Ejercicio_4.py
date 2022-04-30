try:
    numero_1 = int(input("Ingrese un numero: "))
    numero_2 = int(input("Ingrese otro numero: "))
    print(f"Division: ", numero_1 / numero_2)
except ZeroDivisionError:
    print("Error... No se puede dividir entre 0...")
except ValueError:
    print("Ooopss... El valor ingresado no es valido.")
except:
    print("Error desconocido...")