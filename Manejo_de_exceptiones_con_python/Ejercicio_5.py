
try: 
    archivo = open("texto_N5.txt", "w")

    archivo.write("Hola Mundo")
except IOError:
    print("Error de E/S")
except:
    print("Error inesperado")