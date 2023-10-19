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

#curso=Coleccion()
#curso.mostrar_lista()
#------------------------------------------------------------------------------

class Socio:
    def __init__(self,nombre,antiguedad):
        self.nombre=nombre
        self.antiguedad= antiguedad


class Club:
        
        lista_socios=[]

        for i in range(0,3):
            nombre=input('nombre')
            antiguedad=int(input('antiguedad'))
            lista_socios.append(Socio(nombre,antiguedad))



        def mostrar(self):
            self.antig_1=0
            self.socio_antiguo=''

            for i in self.lista_socios:
                if i.antiguedad>self.antig_1:
                    self.socio_antiguo=i.nombre
                    self.antig_1=i.antiguedad
            print ('el socio mas antiguo es: ',self.socio_antiguo,self.antig_1)

            

#clubes=Club()
#clubes.mostrar()
                


            

                


            

        








