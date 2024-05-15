import os


class nodo:
    def __init__(self, raiz, nombre):
        self.raiz = raiz
        self.nombre = nombre
        self.direccion = raiz+ '/' + self.nombre
        self.contenido =os.listdir(self.nombre)


    def resumen (self, archivo):
        with open(archivo, 'a') as archivo:
            archivo.write(' Dirección de la carpeta '+self.direccion + '\n')
            archivo.write(' Carpetas dentro '+ str(self.contenido) + '\n')