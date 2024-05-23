
from nodos import *
import os

Nombre_archivo= 'archivo.txt'

# Obtener el directorio home del usuario
home_dir = os.path.expanduser("~")
raizinput =os.path.expanduser(
    input("Ingrese la dirección de la carpeta enla que quiere iniciar el programa (ejemplo '~/Documentos') :")
    )
print(raizinput)




carpetas = [carpeta for carpeta in os.listdir(raizinput) if os.path.isdir(raizinput + '/' + carpeta)]
print(carpetas)
Nodos = [ nodo(raizinput,carpeta) for carpeta in carpetas]

[item.resumen(Nombre_archivo) for item in Nodos]
