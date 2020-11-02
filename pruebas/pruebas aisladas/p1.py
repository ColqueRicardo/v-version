from tkinter import *  # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)

rc=Tk()
rc.title("Panel de pestañas en Tcl/Tk")
rc.geometry("500x250")
frame1 = Frame(rc,bd=5,cursor="hand1",bg="blue")
frame1.config(width=480,height=320)
frame1.pack(side=BOTTOM)
redbutton = Button(frame1, text="Red", fg="red")
redbutton.pack( side = LEFT)

frame2 = Frame(rc,bd=5,cursor="hand2")
frame2.pack(side=RIGHT)
frame2.config(width=480,height=320)
redbutton2 = Button(frame2, text="Red", fg="red")
redbutton2.pack( side = LEFT)

nt= ttk.Notebook(rc)
redbutton3 = Button(nt, text="Red", fg="red")
redbutton3.pack( side = LEFT)

rc.mainloop()
