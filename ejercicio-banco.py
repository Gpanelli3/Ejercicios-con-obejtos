                
                
                
#DESAFIO 
#un banco tiene 3 clientes que pueden hacer depositos y extracciones 
# se requiere que el banco calcule al finalizar el dia la cantidad de dinero que hay depositado y tambien el saldo que posee cada cliente

class Cliente:
    def __init__(self):
        self.clientes=[]
        self.saldo=0

         

class Banco(Cliente):     
    def __init__(self):

        super().__init__()
        self.depositos=0
        self.extracciones=0

    def ingresoDatos(self):
        self.nombre=input('nombre cliente')
        self.opt=int(input('1-DEPOSITO. 2-EXTRACCIONES'))

    def deposito(self):
        self.depositos=int(input('Ingresar el monto a depositar en el banco'))
        self.saldo=self.depositos
        print('deposito en el banco', self.depositos)


    def extraccion(self):
        self.extracciones=int(input('ingresar el monto a retirar de su cuenta'))
        if self.extracciones < self.saldo:
            print('no puedes extraer esa cantidad')
            print('tu saldo es de: ', self.saldo)
        else:
            self.resto=self.saldo-self.extracciones
            print('Correcto retiro de: ', self.resto)

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



bank=Banco()
bank.menu()









#for i in range(0,3):
            #self.nombre=input('nombre cliente')
            #self.nroCliente=int(input('ingresar su numero de cliente'))

            #opt=int(input('1-depositar, 2-extraccion'))

            #if opt ==1:
                #print('usted eligio depositar')

            #elif opt ==2:
                #print('eligio hacer extraccion')