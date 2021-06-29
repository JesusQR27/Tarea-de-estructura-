class ejercicio12:
    def __init__ (self):
        pass
    def Variables(self):
        print()
        i=1
        suma=0
        x=range(100)
        for i in x:
            suma=suma+i*i
            print("Suma: ",suma)
        print()
        input("enter para salir")    

resultado = ejercicio12()
resultado.Variables()