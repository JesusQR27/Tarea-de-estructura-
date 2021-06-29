class ejercicio14:
    def __init__ (self):
        pass
    def Variables(self):
        print()

        prod=1
        suma=0
        resp=input(str("Quieres ingresar un  numero??  (S/N)"))
        print()
        while resp != "n" and resp!= "N":
            
            num=int(input("Ingrese un numero: "))
            print()
            suma=suma+num
            prod=prod*num
            resp=input(str("Desea continuar (S/N)"))
            print()
        print("""el resultado de la  suma es:""",suma,"""
Total del producto es: """,prod)
          
        print()

        
resultado = ejercicio14()
resultado.Variables()