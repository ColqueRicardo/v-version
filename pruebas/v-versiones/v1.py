from tkinter import *  # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
from os import listdir

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def asignaritemsmenu(menu_items,list):
    for i in range (1,len(list)):
        menu_items.add_command(label=list[i], command = donothing)

def prints():
    if len(direcciones.curselection()) != 0:
        t=direcciones.get(direcciones.curselection()[0])
        print(t)
        x = Label(root, text=t).pack(side=LEFT)


root= Tk()
root.geometry("{0}x{0}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
'''menu'''
menu_bar= Menu(root)
archivos=Menu(menu_bar,tearoff =0)
'''lista y carga'''
itemsmenu=["1","2","3","4","5"]
'''asignaritemsmenu(archivos,itemsmenu)'''
asignaritemsmenu(archivos,itemsmenu)
archivos.add_separator()
archivos.add_command(label = "Exit", command = root.quit)
menu_bar.add_cascade(label="Archivos", menu=archivos)
root.config(menu=menu_bar)

'''administrador de archivos'''
visualizadorbd = Frame(root,bd=5,cursor="hand1",bg="blue").place(x=0,y=0,relwidth=0.15,relheight=0.8)
ruta=StringVar()
direcciones= Listbox(visualizadorbd)
lista_direcciones=StringVar()
lista_direcciones=listdir("C:/Users/ricar/Desktop/Pruebas Bd")

direcciones.place(x=0,y=0,relwidth=0.15,relheight=0.4)
direcciones.insert(0,"das")
t=StringVar()

y=Button(root,text=t,command=prints).pack()

root.mainloop()
