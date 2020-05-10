from tkinter import *  # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
from os import listdir

def ls(ruta = '.'):
    return listdir(ruta)


path = "C:/Users/ricar/Desktop/pruebas v1"
directorios = []
for dir in listdir(path):
    element= {}
    element['directorio'] = dir
    path_nuevo = path +'/'+str(dir)+'/'
    for file in listdir(path):
        element['archivo'] = file
        directorios.append(element)
print (directorios)

'''verificar cual tarda mas un for direccionies in list direcciones o
                                var= list direcciones 
                                for i in range(1.len(direcciones)
                                    considerar por tiempo de memoria)'''
ruta=StringVar()
ruta=ls("C:/Users/ricar/Desktop/pruebas v1")
print (ruta )

