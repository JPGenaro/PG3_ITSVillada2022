class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self) -> str:
        return self.nombre

persona_1 = Persona("Luis")
persona_2 = Persona("Laura")

print(persona_1)
print(persona_2)
