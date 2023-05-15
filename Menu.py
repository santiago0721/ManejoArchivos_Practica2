from Arbol import Arbol

class Menu:

    def __init__(self):
        self.arbol = Arbol()


    def menu(self):
        print("""
        ¡Bienvenido! \n
        [1] Agregar Carpeta
        [2] Agregar Archivo
        [3] Modificar Carpeta
        [4] Modificar Archivo
        [5] Salir       
        """)

        try:
            decision = int(input("Ingrese la opción deseada. \n"))
        except ValueError:
            self.menu()

        if not decision in range(1,6):
            self.menu()

#TERMINAR DECISIONES DEL MENÚ
        if decision == 1:
            carpeta_madre = input("Ingrese el nombre de la carpeta madre.")
            self.arbol.crear_archivo(1, carpeta_madre)
        elif decision == 2:
            carpeta_madre = input("Ingrese el nombre de la carpeta madre.")
            self.arbol.crear_archivo(2, carpeta_madre)
        elif decision == 3:
            nombre_carpeta = input("Ingrese el nombre de la carpeta madre.")
            self.arbol.crear_archivo(2, nombre_carpeta)



a = Menu()
a.menu()
