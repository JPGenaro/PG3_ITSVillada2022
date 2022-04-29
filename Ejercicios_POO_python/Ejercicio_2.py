from xml.dom.minidom import Notation


class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def __str__(self) -> str:
        return f'Nombre: {self.nombre} | Nota: {self.nota}|'

alumno_1 = Alumno('Carlos', 8)
alumno_2 = Alumno('Jose', 4)
alumnos = [alumno_1, alumno_2]

print(f'{alumno_1} \n{alumno_2}')

for i in range(len(alumnos)):
    if alumnos[i].nota >= 7:
        print(f'El alumno {alumnos[i].nombre} esta aprobado.')
    else:
        print(f'El alumno {alumnos[i].nombre} no esta aprobado.')