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

#EJERCICIOS----------------------------------------------------------------

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
                
            
        

agendar=Agenda()
agendar.menu()


#--------------------------------------------------------------------------------------------------------------
