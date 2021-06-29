class ejercicio17:
    def __init__ (self):
        pass
    def Variables(self):
        print() 
        l=1
        n=int(input("ingrese un numero para la serie: "))
        print() 
        s=5
        ser=0
        for a in range(l,n+1):
            s=s+5
            ser=ser+s
        print(" el resultado de la suma de la serie es:", ser)

        print()
     
        
resultado = ejercicio17()
resultado.Variables()