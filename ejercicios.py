#EJERCICIOS

class Promedio:
    def __init__(self):
        self.msje=print('Promedio de notas del alumno')
        self.numero_1=int(input('ingresar la primer nota'))
        self.numero_2=int(input('ingresar la segunda nota'))
        self.numero_3=int(input('ingresar la tercer nota'))
    
    def prom(self):
        promedio=(self.numero_1+self.numero_2+self.numero_3)/3
        print(promedio)


    

#calcPromedio=Promedio()
#calcPromedio.prom()


class Cuadrado:
    def __init__(self):
        self.msje=print('elevar numeros al cuadrado')
        self.numero_1=int(input('ingresar numeros'))
        self.numero_2=int(input('ingresar numeros'))
        self.numero_3=int(input('ingresar numeros'))

    def listar(self):
        nums=[]
        for i in range(0,1):
            nums.append(self.numero_1)
            nums.append(self.numero_2)
            nums.append(self.numero_3)
        eleva=[]
        for i in nums:
            eleva.append(i**2)
        print(eleva)

#aLaDos=Cuadrado()
#aLaDos.listar()



class MostrarNumeros:
    
    numeros=0
    acum=0



    def muestra(self):

        for i in range(0,100):
            self.numeros=int(input('ingresar numeros'))
            if self.numeros == 0:
                break
            else:
                self.acum+=self.numeros
        print('la suma de los numeoros es: ', self.acum)


mynumeros=MostrarNumeros()
mynumeros.muestra()