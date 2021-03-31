nombre = ""

nota1 = 0
nota2 = 0
nota3 = 0

resul = 0

print(nombre)

print("Nombre del estudiante")
nombre=input()

print("Primera nota de "+nombre)
nota1=input()

print("Segunda nota de "+nombre)
nota2=input()

print("Tercera nota de "+nombre)
nota3=input()

resul = (int(nota1) + int(nota2) + int(nota3)) / 3


if resul < 3:
    print("El estudiante "+ nombre +" No se graduo porque saco un puntaje de "+ str(resul))

elif resul >= 3:
    print("El estudiante "+ nombre +" Logro graduarse porque saco un puntaje de "+ str(resul))
    print("Felicidades!!")
