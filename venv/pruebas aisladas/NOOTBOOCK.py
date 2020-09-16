from tkinter import  *
from tkinter import  ttk
def obtener():
    print(text1.get(),text2.get())

vent= Tk()
vent.geometry("250x250")
note = ttk.Notebook(vent)
note.pack(fill="both",expand="yes")

note1 = ttk.Notebook(note)
note1.pack(fill="both",expand="yes")
note.add(note1,text="frame1")

note2 = ttk.Notebook(note)
note2.pack(fill="both",expand="yes")
note.add(note2,text="frame2")

frame4=Frame(note1)
note1.add(frame4,text="hola")

frame5=Frame(note2)
note2.add(frame5,text="hola")

vent.mainloop()
