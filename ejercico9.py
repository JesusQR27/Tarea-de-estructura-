class ejercicio9:
    def __init__ (self):
        pass
    def Variables(self):
        print()
        NUM= int(input("Ingrese la primer variable: "))
        V= int(input("Ingrese la segunda Variable: "))
        print()
        if NUM== 1:
            Resp=100*V
        elif NUM==2:
            Resp=pow(100,V)
        elif NUM==3:
            Resp=100/V
        else:
            Resp=0
                
        print("El  Resultado es:",Resp)
        print()
resultado = ejercicio9()
resultado.Variables()