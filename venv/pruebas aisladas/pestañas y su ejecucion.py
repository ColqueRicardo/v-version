from tkinter import  *
import tkinter as tk
from tkinter import  ttk
from tkinter import messagebox
from pynput.mouse import Button as Mouse_button, Controller
import xml.etree.ElementTree as ET


def archivoxml():
    bd = ET.Element("base")
    ventana = ET.SubElement(bd, "ventana", name="ventana-consultas")
    ventana_hide = ET.SubElement(ventana, "ventana-hide", )
    ventana_hide.set("option-hide", "0")
    ET.dump(bd)
    tree = ET.ElementTree(bd)
    tree.write("C:/Users/ricar/Desktop/pruebas v1/pruebasv1.xml")
def modificar_leer_xml():
    estructura_xml = ET.parse("C:/Users/ricar/Desktop/pruebas v1/pruebasv1.xml")
    # Obtiene el elemento raíz:
    raiz = estructura_xml.getroot()
    print("primer for")
    for elemento_hijo in raiz:
        print(elemento_hijo)
    print("segundo for")

    for ventana in raiz.findall("ventana"):
        print(ventana.find("ventana-consultas"))

    for ventana in raiz.iter('ventana'):
        ventana.text = "nuevotexto"
        ventana.set("option-hide", "1")
        print(ventana.get("option-hide"))

    estructura_xml.write("C:/Users/ricar/Desktop/pruebas v1/pruebasv1.xml")


def opciones(event):
    mouse= Controller()
    mouse.click(Mouse_button.left,1)

    Varialbe_ubicacion = "{0}x{0}+" + str(vent.winfo_pointerx()) + "+" + str(vent.winfo_pointery())
    '''root.geometry("{0}x{0}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))'''
    opciones_vent.geometry(Varialbe_ubicacion.format(175, 40))
    opciones_vent.deiconify()

    '''se a abierto una ventana modificar el xml'''



def crear():

    frame.append(Frame(note))
    frame[len(frame)-1].bind("<<FocusIn>>", f)
    note.add(frame[len(frame) - 1], text="Consulta")
    consulta.append(Entry(frame[len(frame)-1]))
    consulta[len(consulta)-1].place(x=0,y=0,relheight=1,relwidth=1)
    opciones_vent.withdraw()
'''    print("framme")
    print(frame)
    print("text")
    print(consulta)
'''

def hola():
    try:
        indice_notebook_general=note.index(tk.CURRENT)
    except:
        indice_notebook_general=0
    print(indice_notebook_general)
def cerrar():


    note.select(note.index(tk.CURRENT))
    note.forget(note.index(tk.CURRENT))
    frame.pop(note.index(tk.CURRENT))
    consulta.pop(note.index(tk.CURRENT))
    print(len(consulta))
    print(len(frame))
    opciones_vent.withdraw()

    '''    mause.click(vent.winfo_pointerx(),vent.winfo_pointery())'''

def opciones_withdraw():
    '''se a abierto una ventana modificar el xml'''
    estructura_xml = ET.parse("C:/Users/ricar/Desktop/pruebas v1/pruebasv1.xml")
    # Obtiene el elemento raíz:
    raiz = estructura_xml.getroot()

    for ventana in raiz.iter('ventana'):
        if int(ventana.get("option-hide"))==1:
            ventana.set("option-hide","0")
            opciones_vent.withdraw()
        else:
            ventana.set("option-hide","1")
    estructura_xml.write("C:/Users/ricar/Desktop/pruebas v1/pruebasv1.xml")

def esconder_opciones(event):
    opciones_withdraw()
def f(event):
    print("focus")
    print(note.index(tk.CURRENT))

'''    print(str(note.index(ttk.CURRENT())))'''
def notebook_cambio(event):
    print(note.index(tk.CURRENT))
    print("cambio")

'''ButtonRelease-1'''
'''ubicacion[0]--> eje x , [1]-->y'''
def ver():
    print(note.tabs())
    for i in range(len(note.tabs())):
        print(note.tab(i))
'''        print(note.identify(x,y))'''
'''    print(note.tab(0, option=identify(x,y)))
'''

frame=[]
consulta=[]

opciones_vent= Tk()
butons= Button(opciones_vent)
boton_crear = Button(opciones_vent, text="Crear", command=crear,cursor="hand2",relief=FLAT)
boton_crear.place(x=0,rely=0,relheight=0.2,relwidth=1)
boton_cerrar = Button(opciones_vent, text="Cerrar", command=cerrar,cursor="hand2",relief=FLAT)
boton_cerrar.place(x=0,rely=0.2,relheight=0.2,relwidth=1)
opciones_vent.overrideredirect(1)
opciones_vent.geometry("200x100")
opciones_vent.withdraw()

opciones_vent.bind("<FocusOut>",esconder_opciones)


vent= Tk()
vent.geometry("500x250")

note = ttk.Notebook(vent)
note.pack(fill="both",expand="yes")
note.bind("<3>",opciones)

vent.bind("<1>",esconder_opciones)
note.bind("<<NotebookTabChanged>>",notebook_cambio)

boton=Button(vent,command=ver,text="ver").pack()

vent.mainloop()
