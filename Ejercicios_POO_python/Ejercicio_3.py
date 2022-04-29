class Triangulo:
    def __init__(self, lado_1, lado_2, lado_3):
        self.lado_1 = lado_1
        self.lado_2 = lado_2
        self.lado_3 = lado_3
    
    def __str__(self) -> str:
        return f'|Lado 1: {self.lado_1} cm| Lado 2: {self.lado_2} cm| Lado 3: {self.lado_3} cm|'

triangulo_1 = Triangulo(10, 10, 10)
triangulo_2 = Triangulo(10, 5, 12)
triangulo_3 = Triangulo(8, 2, 4)
print(f'Triangulo 1: {triangulo_1}')
print(f'Triangulo 2: {triangulo_2}')
print(f'Triangulo 3: {triangulo_3}')

triangulos = [triangulo_1, triangulo_2, triangulo_3]

#Calculo de los lados
for i in range(len(triangulos)):
    print(f"\nTriangulo {i+1}:\n")
    if triangulos[i].lado_1 == triangulos[i].lado_2 == triangulos[i].lado_3:
        print(f"El triangulo es equilatero. Sus medidas son {triangulos[i]}")
    else:
        if triangulos[i].lado_1 > triangulos[i].lado_2 and triangulos[i].lado_1 > triangulos[i].lado_3:
            print(f"El lado 1 es el mas grande del triangulo, tiene {triangulos[i].lado_1} cm.")
        elif triangulos[i].lado_2 > triangulos[i].lado_1 and triangulos[i].lado_2 > triangulos[i].lado_3:
            print(f"El lado 2 es el mas grande del triangulo, tiene {triangulos[i].lado_2} cm.")
        else:
            print(f"El lado 3 es el mas grande del triangulo, tiene {triangulos[i].lado_3} cm.")