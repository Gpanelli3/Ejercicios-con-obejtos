
#EJERCICIOS----------------------------------------------------------------

#DESAFIO 
#un banco tiene 3 clientes que pueden hacer depositos y extracciones 
# se requiere que el banco calcule al finalizar el dia la cantidad de dinero que hay depositado y tambien el saldo que posee cada cliente

class Cliente():
    def __init__(self):
        self.cliente1=''
         
    def ingreso(self):
            self.person=input('ingrese su nombre de cliente')
            self.cliente1=self.person

            if self.person == self.cliente1:
                print('BIENVENIDO ', self.cliente1)
            
class Banco():     
    def __init__(self):

        self.total_depositado=0
        self.deposito_banco=[]
        
        
        self.saldo=5000


    def deposito(self):
        cliente=Cliente()
        cliente.ingreso()

        while True:
            depositar=int(input('ingresar el monto a depositar'))
            #if depositar<self.saldo1:
                #print('no tiene sufiente saldo, su saldo es de: ', self.saldo1) 
            #else:
            self.total_depositado=(self.saldo+depositar)

            print('lo depositado es: ', depositar)
            print('el saldo que le queda es de: ', self.total_depositado)
            self.deposito_banco.append(depositar)

            salida=input('desea seguir depositando?')
            if salida == 'si':
                True
            else:
                break


    def extraccion(self):
        while True:
            extraer=int(input('ingresa el monto a extraer'))
            extracciones=(self.total_depositado - extraer)

            print('el saldo restante es de: ', extracciones)

            salida=input('desea seguir extrayendo?')
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
        while True:
            opcion=int(input('1-DEPOSITOS. 2-EXTRACCIONES. 3-MOSTRAR DATOS. 4-CERRAR'))

            if opcion==1:
                self.deposito()
            elif opcion==2:
                self.extraccion()
            elif opcion==3:
                self.mostrar()
            elif opcion==4:
                self.cerrar()




#bank=Banco()
#bank.menu()



        
    
#--------------------------------------------------------------------------------------------------------------
class Socio:
    def __init__(self,nombre,antiguedad):
        self.nombre=nombre
        self.antiguedad= antiguedad
        self.lista_socios=[]

        def ingreso(self):
            for i in range(0,3):
                self.nombre=input('nombre')
                self.antiguedad=int(input('antiguedad'))
                self.lista_socios.append(Socio(nombre,antiguedad))

class Club:
        def __init__(self):
            self.antiguo=0
            self.socio_mas_antiguo=''

        def mostrar(self):
            ingreso=Socio()
            ingreso.ingreso()

            for i in self.lista_socios:
                if i.antiguedad>self.antiguo:
                    self.self.socio_mas_antiguo=i.nombre
                    self.antiguo=i.antiguedad
            print ('el socio mas antiguo es: ',self.socio_mas_antiguo,self.antiguo)

#clubes=Club()
#clubes.mostrar()


#--------------------------------------------------------------------------------------------------------------

#Realizar un programa que conste de una clase llamada Alumno 
# que tenga como atributos el nombre y la nota del alumno.
# Definir los métodos para inicializar sus atributos,
#  imprimirlos y mostrar un mensaje con el resultado de la nota y 
# si ha aprobado o no.´


class Estudiante():
    def __init__(self):
        self.nombre=input('ingresar nombre del alumno ')
        self.nota=int(input('nota'))
    
    def mostrarNota(self):
        if self.nota>7:
            print('el alumno', self.nombre, 'aprobo con: ', self.nota)
        else:
            print('el alumno', self.nombre, 'NO aprobo con: ', self.nota)
#estudiante1=Estudiante()
#estudiante1.mostrarNota()

#--------------------------------------------------------------------------------------------------------------


#Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email.
#  Además deberá mostrar un menú con las siguientes opciones

#Añadir contacto
#Lista de contactos
#Buscar contacto
#Editar contacto
#Cerrar agenda


class Agenda():
    def __init__(self):
        self.agenda=[]

    def ingresar(self):
        nombre=input('ingresar nombre')
        telefono=int(input('telefono'))
        email=input('email')
        self.agenda.append({'nombre':nombre,'telefono':telefono,'email':email})
        print('contacto agendado')
        print(self.agenda)
    
    def listarContactos(self):
        if len(self.agenda) == 0:
            print('no hay contactos')
        else: 
            for i in self.agenda:
                print(i)

    def buscarContactos(self):
        for i in range(len(self.agenda)):
            buscar=input("ingresar nombre a buscar")
            if buscar == self.agenda[i]:
                print('encontre a tu contacto', self.agenda[i])
            else:
                print('no existe')

    def editarContacto(self):
        print('editar contacto')
    
    def cerrar(self):
        print('Agenda cerrada')


    def menu(self):
        while True: 
            print('AGENDA')
            self.opt=int(input('1-INGRESAR CONTACTO. 2-LISTAR CONTACTOS. 3- BUSCAR CONTACTOS. 4-EDITAR CONTACTOS. 5-CERRAR AGENDA'))

            if self.opt == 1:
                self.ingresar()
            elif self.opt == 2:
                self.listarContactos()
            elif self.opt == 3:
                self.buscarContactos()
            elif self.opt == 4:
                self.editarContacto()
            elif self.opt == 5:
                self.cerrar()
                break
                
            
        

#agendar=Agenda()
#agendar.menu()
#--------------------------------------------------------------------------------------------------------------
