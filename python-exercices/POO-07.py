# Herecia ejercicio practico 

class Calculadora:
    def __init__(self, numeros):
        self.numeros = numeros 
        self.datos = [0 for i  in range(numeros) ]

    def ingresarDato(self):
        self.datos = [int(input('Ingresar datos: ' + str(i+1) + '= ' )) for i in range(self.numeros) ]

class OpBasica(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 2 )

    def suma(self):
        a,b, = self.datos
        s = a + b

        print ('el resultado es :',s)

    def resta(self):
        a , b = self.datos
        s = a - b

        print ('el resultado es :',s)

class Raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 1)

    def cuadrada(self):
        import math

        a, =self.datos

        print('el resultadop es ', math.sqrt(a) )

ejemplo = OpBasica()


print(ejemplo.ingresarDato())
print(ejemplo.suma())
