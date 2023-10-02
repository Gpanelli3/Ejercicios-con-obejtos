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
otroAuto = Auto()
otroAuto.encender()
#print(otroAuto.encendido)

#instanciar una clase(creamos un objeto)
myAuto=Auto()
#print(myAuto.marca)

#otro auto
myAuto.marca='citroen'
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


