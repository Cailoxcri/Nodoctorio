
from nodos import *
import os

Nombre_archivo= 'archivo.txt'

os.chdir('/home/cailox/Documentos')

carpetas = [carpeta for carpeta in os.listdir() if '.' not in carpeta]

Nodos = [ nodo(os.getcwd(),carpeta) for carpeta in carpetas]

[item.resumen(Nombre_archivo) for item in Nodos]
