class Familia:
    def __init__(self, nombre_padre, nombre_madre, nombre_hijos):
        self.nombre_padre = nombre_padre
        self.nombre_madre = nombre_madre
        self.nombre_hijos = nombre_hijos

    def __str__(self):
        return f'|Nombre del padre: {self.nombre_padre}| Nombre de la madre: {self.nombre_madre}| Nombre de los hijos: {self.nombre_hijos}'

familia_1 = Familia('Raul', 'Maria', ['Juan', 'Jose', 'Ana'])
familia_2 = Familia('Karlos', 'Agos', ['Lisandro', 'Marcos'])

print(familia_1)
print(familia_2)