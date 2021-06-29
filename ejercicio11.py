class ejercicio11:
    def __init__ (self):
        pass
    def Variables(self):
        print()
        C1= float(input("Ingrese su  primer Calificacion: "))
        C2= float(input("Ingrese su  segunda Calificacion: "))
        print()
        if C1>=90 or C2>=90:
            print(("Sus Calificaciones son: {} , {} ").format(C1,C2))
            print("             FELICIDSDES ACEPTADO",)
        else:
            print(("Sus Calificaciones son: {} , {} ").format(C1,C2))
            print("           LO LAMENTAMOS USTED ES RECHAZADO")
        print()
        
        
resultado = ejercicio11()
resultado.Variables()