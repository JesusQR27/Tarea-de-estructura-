class ejercicio2:
    def __init__(self):
        pass
    def Calcular(self):

        print()
        TC=float(input("Ingresa el  total de la compra:"))
        D=TC*0.15
        CP=TC-D
        print()
        print("Su cantidad a pagar es: ")
        print("$",CP)
        print()
        input("enter para salir")

tarea = ejercicio2()
tarea.Calcular()