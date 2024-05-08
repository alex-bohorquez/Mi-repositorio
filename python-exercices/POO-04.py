# funciones para atributos 

class Persona:
    edad = 27 
    nombre  = 'Victor'

doctor = Persona()
print(doctor.edad)

print('El doctor tiene una edad?',hasattr(doctor,'apellido'))

print('Antes era :', doctor.nombre)
setattr(doctor, 'nombre', 'Julian')
print('Ahora es :',  doctor.nombre)
delattr(doctor, 'edad' )
print(doctor.edad)
