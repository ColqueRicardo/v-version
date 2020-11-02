from tkinter import *  # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)

def posicionarmenu(menu,relx):
    menu.place(relx=relx, rely=0.005, relheight=0.025, relwidth=0.1)
    menu.menu = Menu(menu, tearoff=1)
    menu["menu"] = menu.menu

def asignarmenu(menu,nombre,variable):
    menu.menu.add_button ( text= nombre,
                          variable = variable )
'''button = Button(vent, text="prueba", command=radioprueba).place(x=10, y=100)'''
v1= Tk()
v1.geometry("{0}x{1}+0+0".format(v1.winfo_screenwidth(), v1.winfo_screenheight()))
'''v1.overrideredirect(True) pantalla completa '''
cinta= Frame(v1,bg="gray").place(relx=0,rely=0,relwidth = 1 ,  relheight = 0.035 )
'''definicion de menu'''

archivos= Menubutton(cinta,text="Archivos",relief=RAISED)
posicionarmenu(archivos,0.005)

'''define los items del menu y la variable q ocupa (no importa)'''
itemsmenu=["mayo","otro","nose","hola"]
mayoVar  = StringVar()
for i in range (0, len(itemsmenu)):
    asignarmenu(archivos,itemsmenu[i],mayoVar)

'''archivos.menu.add_checkbutton ( label = "mayo",
                          variable = mayoVar )'''
opciones= Menubutton(cinta,text="Opciones",relief=GROOVE)
posicionarmenu(opciones,0.115)
itemsmenu=["mayo","otro"]

for i in range (0, len(itemsmenu)):
    asignarmenu(opciones,itemsmenu[i],mayoVar)


text= Entry(v1,textvariable=mayoVar).pack()


v1.mainloop()


