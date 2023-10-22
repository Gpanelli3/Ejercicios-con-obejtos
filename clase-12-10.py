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
            

                


            

        








