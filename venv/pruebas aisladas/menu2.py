#!/usr/bin/env python
#-*- coding: utf-8 -*-

from Tkinter import *

contador = 0

def actualizar():
    '''Actualiza la entrada de menu.'''
    global contador
    contador += 1
    menu.entryconfig(0, label=str(contador))

raiz = Tk()

# Crear el menu principal
menubarra = Menu(raiz)

# Crear el menu desplegable Prueba
menu = Menu(menubarra, tearoff=0, postcommand=actualizar)
menu.add_command(label=str(contador))
menu.add_command(label="Salir", command=raiz.quit)
menubarra.add_cascade(label="Prueba", menu=menu)

# Mostrar el menu
raiz.config(menu=menubarra)

# Mostrar la ventana
raiz.mainloop()

# Enlazar el menu popup al marco
marco.bind("<Button-3>", popup)

# Mostrar la ventana
raiz.mainloop()