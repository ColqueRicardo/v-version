from tkinter import *  # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
import socket
import sys
import datetime
from tkinter import messagebox
import time
import threading
import random
'sys.path.append("C:/Users/ricar/PycharmProjects/v-version/venv/prueba servidor-cliente/prueba.py")'
import keyboard

class gui_pong():
    def __init__(self):
        self.ventana=Tk()
        self.ventana.geometry("250x250")
        self.inicio_jugadores_y=[]
        self.pelota_x=0
        self.pelota_y=0
        self.conexion=None
        self.boton=Button(self.ventana,command=self.imprimir_conexion(),text="imprimir conexion").pack(side="top")
        self.ventana.mainloop()
    def imprimir_conexion(self):
        print(self.conexion)

d=gui_pong()
