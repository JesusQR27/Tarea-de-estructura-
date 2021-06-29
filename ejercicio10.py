class ejercicio10:
    def __init__ (self):
        pass
    def Variables(self):
        print()
        C1= float(input("Ingrese  la primer Calificacion: "))
        C2= float(input("Ingrese la  segunda Calificacion: "))
        print()
        if C1>=80 and C2>= 80:
            print(("Sus Calificaciones son: {} , {} ").format(C1,C2))
            print("              FELICIDSDES ACEPTADO",)
        else:
            print(("Sus Calificaciones son: {} , {} ").format(C1,C2))
            print("              LO LAMENTAMOS USTED ES RECHAZADO")
        print()
   
        
resultado = ejercicio10()
resultado.Variables()