
class Automovil:
    color = ""

    def acelerar(self):
        print("el auto esta acelerando")

    def frenar(self):
        print("El auto esta frenando")

class Ferrari(Automovil):

    def frenar(self):
        print("El ferrari esta frenando")

class Mercedez (Automovil):
     def frenar(self):
        print("El mercedez esta frenando")

ferrari = Ferrari()
mercedez = Mercedez()

ferrari.frenar()
mercedez.acelerar()

