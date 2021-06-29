class ejercicio5:
    def __init__(self):
        pass
    def Calcular(self):
        print()
        cal=float(input("Ingrese su calificacion:"))
        if cal >= 7 :
            print()
            print("Felicidades por este logro")
            print("       APROBADO")
        else:
            print()
            print("Sigue esforzandote")
            print("          REPROBADO")
        print()
        print()
        

tarea = ejercicio5()
tarea.Calcular()