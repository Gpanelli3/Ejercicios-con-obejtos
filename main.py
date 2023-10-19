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
#DESAFIO 
#un banco tiene 3 clientes que pueden hacer depositos y extracciones 
# se requiere que el banco calcule al finalizar el dia la cantidad de dinero que hay depositado y tambien el saldo que posee cada cliente

class Banco():     
    def __init__(self):
        self.cliente1='Fernando'
        self.cliente2='Agustin'
        self.cliente3='Marcela'

        self.total_depositado=0
        self.deposito_banco=[]
        
        
        self.saldo1=5000
        self.saldo2=12000
        self.saldo3=35000

    def deposito(self):
        while True:
            self.person=input('ingrese su nombre de cliente')
            if self.person == self.cliente1:
                print('BIENVENIDO ', self.cliente1, 'AQUI PUEDE DEPOSITAR SU DINERO')


                depositar=int(input('ingresar el monto a depositar'))
                #if depositar<self.saldo1:
                    #print('no tiene sufiente saldo, su saldo es de: ', self.saldo1) 
                #else:
                self.total_depositado=(self.saldo1-depositar)

                print('lo depositado es: ', depositar)
                print('el saldo que le queda es de: ', self.total_depositado)
                self.deposito_banco.append(depositar)

                salida=input('desea seguir depositando?')
                if salida == 'si':
                    True
                else:
                    break



            elif self.person == self.cliente2:
                print('BIENVENIDO ', self.cliente2)
                depositar=int(input('ingresar el monto a depositar'))

                #if depositar<self.saldo2:
                    #print('no tiene sufiente saldo, su saldo es de: ', self.saldo2) 
                #else:
                self.total_depositado=self.saldo2-depositar

                print('lo depositado es: ', depositar)
                print('el saldo que le queda es de: ', self.total_depositado)
                self.deposito_banco.append(depositar)

                salida=input('desea seguir depositando?')
                if salida == 'si':
                    True
                else:
                    break



            elif self.person == self.cliente3:
                print('BIENVENIDO ', self.cliente3)
                depositar=int(input('ingresar el monto a depositar'))
                #if depositar<self.saldo3:
                    #print('no tiene sufiente saldo, su saldo es de: ', self.saldo3) 
                #else:
                self.total_depositado=self.saldo3-depositar

                print('lo depositado es: ', depositar)
                print('el saldo que le queda es de: ', self.total_depositado)
                self.deposito_banco.append(depositar)

                salida=input('desea seguir depositando?')
                if salida == 'si':
                    True
                else:
                    break

    
    def mostrar(self):
        total_diario=0
        for i in self.deposito_banco:
            total_diario+=i
        print('el total depositado del dia es: ', total_diario)




    def cerrar(self):
        print('saliste correctamente')


    def menu(self):
        print('AGENDA')
        while True: 
            opcion=('1-INGRESAR DATOS. 2-DEPOSITOS. 3-EXTRACCIONES. 4-CERRAR')

            if opcion==1:
                self.deposito()
            elif opcion==2:
                self.extraccion()
            elif opcion==3:
                self.cerrar()
                break



class Cliente():
    def __init__(self):
        #def depositar(self,cantidad,saldo):
            #cantidad=int(input('Ingresar el monto a depositar en el banco'))
            #saldo+=cantidad
            #print('la cantidad depositada es: ', cantidad)
            #print('el saldo es: ', saldo)
        
        def extraer(self,extraccion):
            self.extraccion-=extraccion
            print('el monto extraido es de: ', self.extraccion)
        

bank=Banco()
bank.deposito()
bank.mostrar()
    