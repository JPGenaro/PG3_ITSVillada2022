class Operaciones:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
        self.sumar()
        self.restar()
        self.division()
        self.multiplicar()

    def sumar(self):
        print(f'La suma de {self.num_1} + {self.num_2} = {self.num_1+self.num_2}')
    
    def restar(self):
        print(f'La resta de {self.num_1} - {self.num_2} = {self.num_1-self.num_2}')
    
    def division(self):
        print(f'La division de {self.num_1} / {self.num_2} = {self.num_1/self.num_2}')

    def multiplicar(self):
        print(f'La multiplicacion de {self.num_1} x {self.num_2} = {self.num_1*self.num_2}')

operacion = Operaciones(10, 10)