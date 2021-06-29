class ejercicio15:
    def __init__ (self):
        pass
    def Variables(self):
        print()

        prod=1
        suma=0
        num=int(input("ingrese un numero entero que no sea negativo: "))
        print()
        while num != -1 :
            
            num=int(input("Ingrese un numero: "))
            suma=suma+num
            prod=prod*num
            
            print()
        print("""Total de la suma es:""",suma,"""
Total del producto es: """,prod)
          
        print()
        
        
resultado = ejercicio15()
resultado.Variables()