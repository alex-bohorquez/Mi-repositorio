#Metodo constructor 

#__init__()  -> inhstanciar un nuevo metodoe en esa clase
#            -> Primer metodo para crear un objecto 
#            -> su principla funcion es establecer un estado inicial  en el objeto nada mas instanciarlo, es decir iniciar atributos
#            

class Persona: 
    pass 
    def __init__(self,edad,nombre):
        self.nombre = nombre
        self.edad   = edad

    def descripcion(self):
        return 'Se llama {} y tiene {}.'.format(self.nombre,self.edad)

    def comentario(self, frase):
        return '{} dice:  {}'.format(self.nombre, frase) 

doctor = Persona(33, 'Victor')

print(doctor.descripcion())
print(doctor.comentario('Hola que pes'))

class Email:
    def __init__(self):
        self.enviado = False

    def enviar_correo(self):
        self.enviado = True 

mi_correo = Email()

print(mi_correo.enviado)

mi_correo.enviar_correo()

print(mi_correo.enviado)
