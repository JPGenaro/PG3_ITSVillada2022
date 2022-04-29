class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'|Nombre: {self.nombre}| Edad:{self.edad}|'

name = str(input('Ingrese el nombre: '))
age = int(input('Ingrese la edad: '))
persona_1 = Persona(name, age)
print(persona_1 )
name = str(input('\nIngrese el nombre: '))
age = int(input('Ingrese la edad: '))
persona_2 = Persona(name, age)
print(f'{persona_2}\n')

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
    
    def __str__(self):
        return f'|Nombre: {self.nombre}| Edad: {self.edad}| Sueldo: {self.sueldo}|'

empleado_1 = Empleado(persona_1.nombre, persona_1.edad, 3500)
empleado_2 = Empleado(persona_2.nombre, persona_2.edad, 2850)

print(empleado_1)
print(empleado_2)
empleados = [empleado_1, empleado_2]

for i in range(len(empleados)):
    if empleados[i].sueldo >= 3000:
        print(f"\nEl empleado {empleados[i].nombre} debera pagar impuestos...")
    else:
        print(f"El empleado {empleados[i].nombre} no debera pagar impuestos...\n")