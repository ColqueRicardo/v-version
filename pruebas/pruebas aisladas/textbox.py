from tkinter import  *
from tkinter import  ttk

def obt():
    print(textbox.get())

v= Tk()
v.geometry("500x500")
textbox= Entry(v)
textbox.pack()
b= Button(v,command=obt).place(x=50,y=50,width=30,height=20)
v.mainloop()