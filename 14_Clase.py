# CLASE

class Persona:

    noPies = 2
    noManos = 2
   
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


    def saludar(self):
        print(" esta diciendo hola")

    def despedirse(self):
        print("Adios")


dani = Persona("Daniel", "Jimenez", 24)

print(Persona.noManos)