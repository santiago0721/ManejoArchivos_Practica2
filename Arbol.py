from Carpeta import *
from Archivo import *


class Arbol:

    def __init__(self):
        self.raiz = Carpeta("Raíz")

    def crear_carpeta(self):
        nombre = input("Ingrese el nombre de la carpeta")
        carpeta_nuevo = Carpeta(nombre)
        return carpeta_nuevo

    #IMPLEMENTAR EXCEPCIONES
    def crear_archivo(self):
        nombre = input("Ingrese el nombre del archivo")
        extension = input("Ingrese la extensión")
        peso = input("Ingrese el peso")
        archivo_nuevo = Archivo(nombre, extension, peso)
        return archivo_nuevo

    #IMPLEMENTAR RECORRER
    def agregar(self, decision, nombre_carpeta_madre):
        if decision == 1:
            archivo = self.crear_archivo()
        else:
            carpeta = self.crear_carpeta()
            
    def modificar_archivo(self):
        pass

    def modificar_nombre_carpeta(self):
        pass


a = Arbol()
print(a.raiz)