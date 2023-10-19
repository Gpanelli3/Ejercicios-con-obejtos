                
                
                
#DESAFIO 
#un banco tiene 3 clientes que pueden hacer depositos y extracciones 
# se requiere que el banco calcule al finalizar el dia la cantidad de dinero que hay depositado y tambien el saldo que posee cada cliente

class Banco():     
    def __init__(self):
        self.cliente1='Fernando'
        self.cliente2='Agustin'
        self.cliente3='Marcela'
        
        self.saldo1=0
        self.saldo2=0
        self.saldo3=0

    def deposito(self):
        self.person=input('ingrese su nombre de cliente')
        if self.person == self.cliente1:
            self.cliente1.depositar()

        elif self.person == self.cliente2:
            self.cliente2.depositar()

        elif self.person == self.cliente3:
            self.cliente3.depositar()
    
    def extraccion(self):
        self.cliente1.extraer()
        self.cliente2.extraer()
        self.cliente3.extraer()



    def cerrar(self):
        print('saliste correctamente')

    def menu(self):
        while True:
            print('Menu del banco')
            self.opcion=('1-INGRESAR DATOS. 2-DEPOSITOS. 3-EXTRACCIONES. 4-CERRAR')
    
            if self.opcion==1:
                self.ingresoDatos()
            elif self.opcion==2:
                self.deposito()
            elif self.opcion==3:
                self.extraccion()
            elif self.opcion==4:
                self.cerrar()
                break




class Cliente():
    def __init__(self):
        
        def depositar(self,cantidad):
            self.cantidad=int(input('Ingresar el monto a depositar en el banco'))
            return cantidad
        
        def extraer(self,extraccion):
            self.extraccion-=extraccion
            print('el monto extraido es de: ', self.extraccion)








        


         

