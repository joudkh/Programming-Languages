# tkinter
from tkinter import *
window=Tk()
window.title("First Form")
window.geometry('500x300')


lbl=Label(window,text='hi',bg="red")
lbl.grid(column=0,row=0)

#lbl2=Label(window,text='Hello',font=("Arial Bold", 50))
#lbl2.grid(column=1,row=1)

ent=Entry(window)
ent.grid(column=0,row=1)

def clicked():
   value=ent.get()
   lbl.configure(text=value)

btn=Button(window,text="Click me",bg="yellow",fg="red",command=clicked)
btn.grid(column=0,row=2)





