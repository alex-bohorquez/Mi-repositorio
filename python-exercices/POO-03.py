#METODOS

#CLASS nombre de la clase:
#   DEF nombre del metodo (SELF):
#SELF.nombre de la varible = ALGORITMO

class Matematica:
    def suma(self):
        self.n1 = 2
        self.n2 = 10

s = Matematica()

s.suma()

print(s.n1)

# __init__(SEFT)

class Ropa:
    def __init__(self):
        self.marca = 'Only'
        self.talla = 'M'
        self.color = 'Roja'

pantalon =  Ropa()
print(pantalon.talla)
print(pantalon.marca)
print(pantalon.color)

class Calculadora:
    def __init__(self,a,b):
        self.suma = a + b
        self.resta = a - b 
        self.producto = a * b
        self.division = a / b

operacion = Calculadora(12,41)

print(operacion.resta)

