#interaccion entre clases 

class Persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
class Coleccion:
    lista_alumnos=[]
    lista_alumnos.append(Persona('hugo', 'perez',2))
    lista_alumnos.append(Persona('paco', 'lopez',40))
    lista_alumnos.append(Persona('juan', 'martinez',50))

    def mostrar_lista(self):
        for elemento in self.lista_alumnos:
            print(elemento.nombre,elemento.apellido,elemento.edad)

curso=Coleccion()
curso.mostrar_lista()


class Socio:
    def __init__(self,nombre,antiguedad):
        self.nombre=nombre
        self.antiguedad= antiguedad


class Club:
        lista_socios=[]
        antig_1=0


        for i in range(0,3):
            nombre=input('nombre')
            antiguedad=int(input('antiguedad'))

            
            if antiguedad>antig_1:
                #lista_socios = []
                lista_socios.append(Socio(nombre,antiguedad))
                antiguedad=antig_1
                


        def mostrar(self):
            for i in self.lista_socios:
                print ('el socio mas antiguo es: ', i.nombre,i.antiguedad)
            

#clubes=Club()
#clubes.mostrar()

                


            

        








