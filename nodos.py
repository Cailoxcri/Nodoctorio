import os
Nombre_archivo= 'archivo.txt'

def salto(string):
    with open('Cambio','+r') as linea:
        salto = linea.read()
    
    return salto.replace('Remplazar',str(string))

class nodo:
    
        

    def __init__(self, raiz, nombre):
        self.raiz = raiz
        self.nombre = nombre
        self.direccion = raiz+ '/' + self.nombre
        self.nivel = self.direccion.count('/')
        self.contenido =os.listdir(self.direccion)
        self.carpetas = [carpeta for carpeta in self.contenido if os.path.isdir(self.direccion +  '/' + carpeta)]
        self.ramas = [nodo(self.direccion,carpeta) for carpeta in self.carpetas]
        [item.resumen(Nombre_archivo) for item in self.ramas]

    def resumen (self, archivo):
        if self.carpetas != []:
            with open(archivo, 'a') as archivo:
                archivo.write(' Dirección de la carpeta '+self.direccion  + '\n' )
                archivo.write(' Carpetas dentro '+ str(self.carpetas) + '\n')
                archivo.write( salto(self.nivel))