from tkinter import *  # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
import os
from os import listdir

'''armar listado de rutas'''
def carga(vector,ruta,vector2,pos):
    for elemento in listdir(ruta):
        tab= "\t"*pos
        print( tab, elemento , pos)
        vector.append(elemento)
        vector2.append(pos)
        if(os.path.isdir(ruta+"/"+elemento)):
            carga(vector,ruta+"/"+elemento,vector2,pos+1)
'''simplificacion: falta validar el archivo .prop que tengo q crear para usar, configurar otra pestaña de prop y darle esas prop 
los archivos tambien verificar las extenciones y la ruta ingresada'''
def simplificacion (evento):
    '''si es un directorio abre todo si no configurar extenciones'''
    print(rutas[list.curselection()[0]])
    if(archivos_tipo[list.curselection()[0]]=="carpeta"):
        if(estado[list.curselection()[0]]==0):
            '''0 --> cerrado , 1 --> abierto'''
            estado[list.curselection()[0]]=1
            '''si la seleccion actual es un directorio se guarda asi > sino asi "   " '''
            for elemento in listdir(rutas[list.curselection()[0]]+"/"+ list.get(list.curselection()[0])[3*posicion[list.curselection()[0]]+1:]):
                posicion.insert(list.curselection()[0] + 1, posicion[list.curselection()[0]] + 1)
                if os.path.isdir(rutas[list.curselection()[0]]+"/"+ list.get(list.curselection()[0])[3*posicion[list.curselection()[0]]+1:]+"/"+elemento):
                    archivos_nombre.insert(list.curselection()[0]+1,"   "*posicion[list.curselection()[0]+1]+">"+elemento)
                    archivos_tipo.insert(list.curselection()[0]+1,"carpeta")
                    rutas.insert(list.curselection()[0]+1,rutas[list.curselection()[0]]+"/"+ list.get(list.curselection()[0])[3*posicion[list.curselection()[0]]+1:])
                else:
                    archivos_nombre.insert(list.curselection()[0] + 1,"   " * posicion[list.curselection()[0] + 1] + "   " + elemento)
                    archivos_tipo.insert(list.curselection()[0]+1,"archivo")
                    rutas.insert(list.curselection()[0]+1,rutas[list.curselection()[0]]+"/"+ list.get(list.curselection()[0])[3*posicion[list.curselection()[0]]+1:])
                estado.insert(list.curselection()[0]+1,0)
            list.delete("0","end")
            for i in range(0,len(archivos_nombre)):
                list.insert(i,str(archivos_nombre[i]))
        else:

            '''si ya esta abierto el directorio'''
            estado[list.curselection()[0]]=0

            while posicion[list.curselection()[0]]<posicion[list.curselection()[0]+1]:
                posicion.pop(list.curselection()[0]+1)
                archivos_nombre.pop(list.curselection()[0]+1)
                rutas.pop(list.curselection()[0]+1)
                estado.pop(list.curselection()[0]+1)
            list.delete("0","end")
            for i in range(0,len(archivos_nombre)):
                list.insert(i,str(archivos_nombre[i]))
    else:
        print("es un archivo")

def iniciar():
    for elemento in listdir("C:/Users/ricar/Desktop/pruebas v1"):
        rutas.append("C:/Users/ricar/Desktop/pruebas v1")
        posicion.append(0)
        estado.append(0)
        if os.path.isdir("C:/Users/ricar/Desktop/pruebas v1/"+elemento):
            archivos_tipo.append("carpeta")
            archivos_nombre.append(">"+elemento)
        else:
            archivos_nombre.append("   "+elemento)
            archivos_tipo.append("archivo")
        '''cambiar por cuando solo tenga una extencion'''
    for i in range (0,len(archivos_nombre)):
        list.insert(i,archivos_nombre[i])
    print(rutas)
def hola(evento):
    if len(list.curselection()) != 0:
        c=list.get(list.curselection()[0])
        prueba2 = Entry(rc, text=c,bd=5,bg="blue").pack(side=RIGHT)
        '''define el elemento y el indice'''
        print(c,list.curselection()[0])
''' carga todo como si estubiera abierto
r="C:/Users/ricar/Desktop/pruebas v1"
carga(vec,r,posicion,0)
for i in range(0,len(vec)):
    list.insert(i,"     "*posicion[i]+str(vec[i]))
'''
'''def simplificacion (evento):
    if(os.path.isdir(rutas[list.curselection()[0]]+"/"+ list.get(list.curselection()[0])[4*posicion[list.curselection()[0]]:])):
        if(estado[list.curselection()[0]]==0):
            estado[list.curselection()[0]]=1

            for elemento in listdir(rutas[list.curselection()[0]]+"/"+ list.get(list.curselection()[0])[4*posicion[list.curselection()[0]]:]):
                if os.path.isdir(rutas[list.curselection()[0]]+"/"+ list.get(list.curselection()[0])[4*posicion[list.curselection()[0]]:]):
                    posicion.insert(list.curselection()[0] + 1, posicion[list.curselection()[0]] + 1)
                    archivos_nombre.insert(list.curselection()[0]+1,"   "*posicion[list.curselection()[0]+1]+">"+elemento)
                    rutas.insert(list.curselection()[0]+1,rutas[list.curselection()[0]]+"/"+ list.get(list.curselection()[0])[4*posicion[list.curselection()[0]]:])
                    estado.insert(list.curselection()[0]+1,0)
            list.delete("0","end")
            for i in range(0,len(archivos_nombre)):
                list.insert(i,str(archivos_nombre[i]))
        else:

            estado[list.curselection()[0]]=0

            while posicion[list.curselection()[0]]<posicion[list.curselection()[0]+1]:
                posicion.pop(list.curselection()[0]+1)
                archivos_nombre.pop(list.curselection()[0]+1)
                rutas.pop(list.curselection()[0]+1)
                estado.pop(list.curselection()[0]+1)
            list.delete("0","end")
            for i in range(0,len(archivos_nombre)):
                list.insert(i,str(archivos_nombre[i]))
    else:
        print("es un archivo")

def iniciar():
    for elemento in listdir("C:/Users/ricar/Desktop/pruebas v1"):
        archivos_nombre.append(elemento)
        rutas.append("C:/Users/ricar/Desktop/pruebas v1")
        posicion.append(0)
        estado.append(0)
        if os.path.isdir("C:/Users/ricar/Desktop/pruebas v1/"+elemento):
            archivos_tipo.append("carpeta")

    for i in range (0,len(archivos_nombre)):
        list.insert(i,archivos_nombre[i])'''

def prueba():
    print("archivos _ nombre")
    print(archivos_nombre)
    print("posicion")
    print(posicion)
    print("estado")
    print(estado)
    print("ruta")
    print(rutas)
    print("tipos de archivos")
    print(archivos_tipo)

archivos_nombre=[]
posicion=[]
estado=[]
rutas=[]
archivos_tipo=[]
rc= Tk()
'''rc.geometry("{0}x{0}+0+0".format(rc.winfo_screenwidth(), rc.winfo_screenheight()))'''
rc.geometry("500x500")
list = Listbox(rc,exportselection=0)
'''LISTBOX.SIZE() -->OBTIENE todos los elementos, exportseleccion permite q no se pierda la seleccion al perder el foco ,selectmode=SINGLE'''
iniciar()
list.bind('<<ListboxSelect>>', simplificacion)
list.place(x=0,y=0,relwidth=0.5,relheight=0.5)

but=Button(rc,command=prueba,text="hola").pack()
rc.mainloop()