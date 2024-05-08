#Herencia
#clase Combre sub clase(nombre Clase)

#class ClaseBase:
#   Cuerpo de la clase  
#
#class Derivadoclase (ClseBase)
#   Cuerpo der lca clse deribada
#

class Pokemon:
    pass
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo   = tipo
    def descripcion(self):
        return '{} es un pokemon de tipo {}'.format(self.nombre, self.tipo)

pikachu = Pokemon('pikachu','electrico')
print(pikachu.descripcion())

class Pikachu(Pokemon):
    def ataque(self, tipo_ataque):
        return '{} tipo de ataque {}'.format(self.nombre, tipo_ataque)

class Charmander(Pokemon):
    def ataque(self, tipo_ataque):
        return '{} tipo de ataque {}'.format(self.nombre, tipo_ataque)

nuevo_pokemon = Charmander('boby','electrico')


    
print(nuevo_pokemon.descripcion())

print(nuevo_pokemon.ataque('Bola de fuego'))
