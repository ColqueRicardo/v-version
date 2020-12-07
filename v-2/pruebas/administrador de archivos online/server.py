import socket
import pickle
import threading
import time
import random
import sys
sys.path.append("v-2/pruebas/administrador de archivos online/gestor_file.py")
from gestor_file import *


class cliente:
    def __init__(self):
        self.ruta=[]
    def conectar(self,ip_servidor):
        self.ip_servidor=ip_servidor
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ip_servidor, 8000))
        self.id=pickle.dumps(self.socket.recv(1024))
        return pickle.dumps(self.socket.recv(1024))

    def accion(self,peticion):
        self.socket.send(pickle.loads(peticion))
        return pickle.dumps(self.socket.recv(1024))

class server:
    def __init__(self,conexiones_maximas,puerto,archivos):
        self.ip_server=socket.gethostbyname(socket.gethostname())
        'self.puertos=[]'
        self.puerto_libre=puerto
        self.max_conecciones=conexiones_maximas
        self.hilos=[]
        self.socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('', 8000))
        self.socket.listen(self.max_conecciones)
        self.conexiones=[]
        self.gestor_archivos=archivos
        self.contenidos_archivos=archivo_contenido()
        'clientes'
        self.ruta_actual={}


    def iniciar_server(self):
        self.conexion_id=0
        while True:
            self.conexiones.append(0)
            'self.conexiones[self.conexion_id], direccion = self.conexiones.accept()'
            conexion , direccion = self.conexiones.accept()
            self.hilos.append(threading.Thread(name=str(self.conexion_id), target=self.gestor_conexiones,args={conexion,self.conexion_id}))
            self.hilos[self.conexion_id].start()
            self.conexion_id+=1
    def gestor_conexiones(self,conexion,id_hilo):
        self.ruta_actual[id_hilo]=[]
        self.ruta_actual[id_hilo].append(0)
        'enviarle el sistema de archivos actual desde el master'
        conexion.send(pickle.dumps(id_hilo))
        conexion.send(pickle.dumps(self.gestor_archivos.busqueda_carpeta(self.ruta_actual[id_hilo])))
        while True:
            peticion= pickle.loads(conexion.recv(1024))
            'todas las peticiones tiene el primer dato como lo que necesitan hacer y el segundo la ruta en string, exepcion de creacion de archivo que viene el archivo'
            'peticion[0]= accion , pet[1]=situacion actual(nuevo elemento para la ruta), pet[2]=id del cliente, el resto es un caso especial'
            if peticion[0]=="abrir":
                self.ruta_actual[peticion[2]].append(peticion[1])
                conexion.send(pickle.dumps(self.abrir(self.ruta_actual[peticion[2]])))

            elif peticion[0]=="borrar":

                self.borrar(self.ruta_actual[peticion[2]]+peticion[1])
                conexion.send(pickle.dumps(self.abrir(self.ruta_actual[peticion[2]])))

            elif peticion[0] == "crear_carpeta":

                self.crear_carpeta(self.ruta_actual[peticion[2]])
                conexion.send(pickle.dumps(self.abrir(self.ruta_actual[peticion[2]])))

            elif peticion[0] == "crear_archivo":
                'caso especial peticion => 0 es accion , 1 es archivo,2 es id, 3 es contenido'
                self.crear_archivo(self.ruta_actual[peticion[2]],peticion[1],peticion[3])
                conexion.send(pickle.dumps(self.abrir(self.ruta_actual[peticion[2]])))


    def abrir(self,ruta):
        'abre un archivo o carpeta, o vuelve a la carpeta anterior (caso especial) '
        'falta tratar archivos'
        try:
            return self.gestor_archivos.busqueda_carpeta(ruta)
        except:
            print("recarge todo porque esta mal")
            return "error"

    def borrar(self,ruta):
        'borra una carpeta o archivo'
        try:
            self.gestor_archivos.busqueda_carpeta(ruta).borrar()

        except:
            print("no hay tal elemento o ya se borro")

    def crear_carpeta(self,ruta):
        'crea una carpeta'
        i=0
        while True:
            if self.gestor_archivos.busqueda_carpeta(ruta).agregar_contenido(carpeta("nueva carpeta"+str(i)))!=-1:
                break
            else:
                i+=1

    def crear_archivo(self,ruta,archivo,contenido):
        'crea un archivo'
        if self.gestor_archivos.busqueda_carpeta(ruta).agregar_contenido(archivo)!=-1:
            ruta.append(archivo.nombre+"."+archivo.extencion)
            self.gestor_archivos.busqueda_carpeta(ruta).asigna_contenido(self.contenidos_archivos.agregar(contenido))
        else:
            i=0
            nombre=archivo.nombre
            while  True:
                archivo.nombre=nombre+"copia " + str(i)
                if self.gestor_archivos.busqueda_carpeta(ruta).agregar_contenido(archivo) != -1:
                    ruta.append(archivo.nombre + "." + archivo.extencion)
                    self.gestor_archivos.busqueda_carpeta(ruta).asigna_contenido(self.contenidos_archivos.agregar(contenido))
                    break




ax=archivo_contenido()
sistema_de_archivos=carpeta("master")
for i in range(10):
    sistema_de_archivos.agregar_contenido(archivo(str(i) + ".exe",ax.cantidad_archivos()))
sistema_de_archivos.agregar_contenido(carpeta("carpeta  2"))
sistema_de_archivos.agregar_contenido(carpeta("carpeta  1"))
for i in sistema_de_archivos.contenido:
    if type(i) == carpeta:
        for l in range(5):
            i.agregar_contenido(archivo(str(l) + ".jpg",ax.cantidad_archivos()))

'recorrer(self.sistema_de_archivos)'

server(2,8000,sistema_de_archivos)