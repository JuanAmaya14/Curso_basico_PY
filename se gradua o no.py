def Proceso(nombre, nota1, nota2, nota3):
    Prom = (nota1 + nota2 + nota3) / 3
    Prom = round(Prom, 1)
        
    condicion(nombre, Prom)

def condicion(nombre, Prom):
    if Prom < 3:
        return print(f'El estudiante {nombre} no se graduo porque saco un puntaje de {Prom}')
    else:
        return print(f'El estudiante {nombre} Logro graduarse porque saco un puntaje de {Prom}')
        #return print("Felicidades!!")

def run():
    nombre = input("Nombre del estudiante: ")
    nota1 = int(input(f'Primera nota de {nombre}: '))
    nota2 = int(input(f'Segunda nota de {nombre}: '))
    nota3 = int(input(f'Tercera nota de {nombre}: '))

    Proceso(nombre, nota1, nota2, nota3)

run()