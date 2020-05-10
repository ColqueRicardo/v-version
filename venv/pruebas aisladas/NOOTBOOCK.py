from tkinter import  *
from tkinter import  ttk
def obtener():
    print(text1.get(),text2.get())

vent= Tk()
vent.geometry("250x250")
note = ttk.Notebook(vent)
note.pack(fill="both",expand="yes")
frame1= Frame(note)
frame2= Frame(note)
frame3= Frame(note)
note.add(frame1,text="frame1")
note.add(frame2,text="frame2")
note.add(frame3,text="Frame3")
text1= Entry(frame1)
text1.place(x=10,y=20)
text2= Entry(frame2)
text2.place(x=10,y=20)
button= Button(frame3,command=obtener)
button.pack()
vent.mainloop()
