def Operacion(Notas1 , Notas2):
    Notas1 = Notas1 / 3
    Notas2 = Notas2 / 3

    Notas1 = round(Notas1, 1)
    Notas2 = round(Notas2, 1)

    return (Notas1, Notas2)

def Run():
    Estudiante1 = ["", 0, 0, 0]
    Estudiante2 = ["", 0, 0, 0]


    Estudiante1[0] = input("Nombre del primer estudiante: ")
    Estudiante1[1] = int(input("Primera nota de " + Estudiante1[0] + ": "))
    Estudiante1[2] = int(input("Segunda nota de " + Estudiante1[0] + ": "))
    Estudiante1[3] = int(input("Tercera nota de " + Estudiante1[0] + ": "))

    Estudiante2[0] = input("Nombre del Segundo estudiante: ")
    Estudiante2[1] = int(input("Primera nota de " + Estudiante2[0] + ": "))
    Estudiante2[2] = int(input("Segunda nota de " + Estudiante2[0] + ": "))
    Estudiante2[3] = int(input("Tercera nota de " + Estudiante2[0] + ": "))

    Notas1 = Estudiante1[1] + Estudiante1[2] + Estudiante1[3]
    Notas2 = Estudiante2[1] + Estudiante2[2] + Estudiante2[3] 

    Operacion(Notas1 , Notas2)

    Re1 = Notas1
    Re2 = Notas2


    if Re1 > Re2: 

        print(str(Estudiante1[0]) + " saco un puntaje de " + str(Re1))
        print(str(Estudiante2[0]) + " saco un puntaje de " + str(Re2))
        print(str(Estudiante1[0]) + " gano")

    elif Re1 < Re2:

        print(str(Estudiante1[0]) + " saco un puntaje de " + str(Re1))
        print(str(Estudiante2[0]) + " saco un puntaje de " + str(Re2))
        print(str(Estudiante2[0]) + " gano")

    elif Re1 == Re2:

        print(str(Estudiante1[0]) + " saco un puntaje de " + str(Re1))
        print(str(Estudiante2[0]) + " saco un puntaje de " + str(Re2))
        print("Empate")

Run()