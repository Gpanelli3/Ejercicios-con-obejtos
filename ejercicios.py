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


#mynumeros=MostrarNumeros()
#mynumeros.muestra()



class Persona():

    def iniciali(self,nombre):
        self.nombre = nombre
    
    def mostrar(self):
        print('el nombre es:', self.nombre)
    
#persona1=Persona()
#persona1.iniciali('gena')
#persona1.mostrar()


class Alumno:
    def __init__(self):
        self.nombre=input('nombre')
        self.apellidos=input('apellidos')

    def mostrar(self):
        print('nombre', self.nombre, self.apellidos)

class Profesor(Alumno):
    def __init__(self):
        super().__init__()
        self.sueldo=int(input('ingrese su sueldo'))
    
    def pagarImpuestos(self):
        if self.sueldo>3000:
            print('debe pagar impuestos')
        else:
            print('no debe pagar impuestos')


#alumno1=Alumno()
#alumno1.mostrar()

#profesor1=Profesor()
#profesor1.mostrar()
#profesor1.pagarImpuestos()

#--------------------------------------------------------------------------------------------------------------
#Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__.
#Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. 
#Llamar a la clase Calculadora.

class Calculadora:
    def __init__(self):
        self.valor1=int(input('valor1'))
        self.valor2=int(input('valor2'))

    def suma(self):
        print(self.valor1+self.valor2)

    def resta(self):
        print(self.valor1-self.valor2)

    def mult(self):
        print(self.valor1*self.valor2)

    def div(self):
        print(self.valor1/self.valor2)
#calcu=Calculadora()
#calcu.suma()
#calcu.resta()
#calcu.mult()
#calcu.div()

#-------------------------------------------------------------------------------------------------------------




        
#----------------------------------------------------------------
#Las FUNCIONES son CLAVES, hay que utilizarlas siempre que podamos. Sino tambien utilizarla para empaquetar cosas,
#nos hara el codigo mas mantenible.

#OBJETOS tenemos todo junto, por un lado tenemos las caracteristicas(atributos) y por otro el comportamiento que tienen esos datos(metodos)
#Una clase es algo general, despues podemos modificar esas clases y tranformamos en objetos que es lo particular


#clase
class Auto:
    marca='fiat'
    color='white'
    aceleracion=40
    combustible=10
    encendido=False

    def encender(self):
        self.encendido=True #SELF hace referencia a un dato de la propia clase

#creamos otro objeto y llamamos al metodo encender() 
#otroAuto = Auto()
#otroAuto.encender()
#print(otroAuto.encendido)

#instanciar una clase(creamos un objeto)
myAuto=Auto()
#print(myAuto.marca)

#otro auto
#myAuto.marca='citroen'
#print(myAuto.marca)



class Persona:
    nombre=''
    apellido=''

    def mostrar(self):
        print(self.nombre)
        print(self.apellido)





#CONSTRUCTOR

class Calculadora:
    def __init__(self):
        self.msje=print('Caluladora')
        self.numero_1=int(input('ingresar el primer numero'))
        self.numero_2=int(input('ingresar el segundo numero'))

    def sumar(self):
        suma=self.numero_1+self.numero_2
        print(suma)

#myCalculadora=Calculadora()
#myCalculadora.sumar()

#------------------------------------------------------------------------------




            
                

