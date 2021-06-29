class ejercicio18:
    def __init__(self):
        pass
    def Factorial(self):
        print()
        numero=int(input("Ingrese un numero: "))
        acu=1
        for num in range(numero,1,-1):
            acu =acu*num
        print()
        print("numero:  {}  ,Factorial:  {} ".format(numero,acu))

        print()
        

tarea=ejercicio18()
tarea.Factorial()