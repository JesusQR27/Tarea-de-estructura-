class ejercicio6:
    def __init__(self):
        pass
    def Calcular(self):
        print()
        SUELDO=float(input("Sueldo de empleados:"))
        if SUELDO < 600:
            NS=SUELDO + SUELDO*0.1
            print()
        else:
            NS=SUELDO
            print()
        print()    
        print(NS)
        print()

tarea=ejercicio6()
tarea.Calcular()