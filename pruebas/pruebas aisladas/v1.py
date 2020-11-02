from tkinter import *  # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)

def cargardato():
    if textvariable.get()=="":
        list.append(" ")
    else:
        list.append(textvariable.get())
    muestral.set("")
    for i in range(0, len(list)):
        muestral.set(muestral.get() + list[i])
    print(list)
rc= Tk()
rc.geometry("500x500")
#cargar
list = []
#text
textvariable=StringVar()
text=Entry(rc,text="Escriba",textvariable=textvariable).place(x=30,y=10)
boton = Button(rc,text="cargar",command=cargardato,cursor="hand1",width=35).place(x=30,y=50)
#mostrar
muestral= StringVar()
muestralista=Entry(rc,textvariable=muestral).place(x=30,y=100)
rc.mainloop()