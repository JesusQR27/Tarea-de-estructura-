class ejercicio7:
    def __init__(self):
        pass
    def CalcularJornada(self):
    
        ht,he,het=0,0,0
        ph,phe,pt,ph8=0,0,0,0
        print()
        ht=int(input("Ingrese  Las Horas Trabajadas: "))
        ph=float(input("ingrese  el valor por horas: "))
        if ht > 40:
            he=ht-40
            if he > 8:
                het=he-8
                ph8=8*ph*2
                phe=het*ph*3
            else:
                ph8=he*ph*2
            pt=ph*40+phe+ph8
        else:
            pt= ht*ph
            print()
        print()    
        print("Sobretiempo <8 :{} Sobretiempo >8: {} El pago total de horas trabajadas es:$ {}".format(ph8,phe,pt))
        print()
        
tarea= ejercicio7()
tarea.CalcularJornada()