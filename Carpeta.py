class Carpeta:

    def __init__(self, nombre):
        self.nombre_carpeta = nombre
        self.cant_elementos = 0
        self.espacio1 = None
        self.espacio2 = None
        self.espacio3 = None
        self.espacio4 = None

    def agregar(self, data):
        if self.cant_elementos < 4:  #agregar revisando si hay espacio
            if self.espacio1 is None:
                self.espacio1 = data
            elif self.espacio2 is None:
                self.espacio2 = data
            elif self.espacio3 is None:
                self.espacio3 = data
            else:
                self.espacio4 = data
            return True
        else:
            return False  #Si ya está llena