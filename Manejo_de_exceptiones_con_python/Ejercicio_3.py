tupla: tuple = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
buscador = int(input('Ingrese el numero del mes: '))

try:
    for i in range(len(tupla)):
        if i == buscador:
            print(tupla[i])
            break
except IndexError:
    print('El numero ingresado no corresponde a un mes')
except:
    print('Error desconocido. Pruebe de nuevo...')