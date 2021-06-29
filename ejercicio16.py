class ejercicio16:
    def __init__ (self):
        pass
    def Variables(self):
        print() 
        primo= 0
        divisor=2
        num=int(input("ingrese un numero entero : "))
        print()
        
        while divisor < num and primo ==0 :
            Res= num%divisor
            print(Res)
            if Res == 0:
                primo+=1
            divisor+=1
        if primo ==0:
            print("Numero",num,"es primo")
        else:
            print("Numero",num,"no es primo")
                       
            print()
                  
        print()
       
resultado = ejercicio16()
resultado.Variables()