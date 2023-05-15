class Archivo:

    def __init__(self, nombre, extension, peso):
        self.nombre_archivo = nombre
        self.extension = extension
        self.peso = peso

    def __repr__(self):
        return self.nombre_archivo + "." + self.extension + " " + self.peso
