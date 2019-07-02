from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

# Add a Combobox widget
######################################################
combo=Combobox(window)
combo['values']=(1,2,3,4,5,"hi",7,8,9)
combo.current(5)
combo.grid(column=0, row=0)
######################################################
######################################################


# Add a Radiobutton widget
######################################################
selected=IntVar()
rb1=Radiobutton(window,text="male",value=1,variable=selected)
rb1.grid(column=0, row=1)
rb2=Radiobutton(window,text="female",value=2,variable=selected)
rb2.grid(column=1, row=1)
######################################################
######################################################


# Add a Checkbutton widget
######################################################
chbselection=IntVar()
chb=Checkbutton(window,text="Single",variable=chbselection)
chb.grid(column=0, row=2)
######################################################
######################################################


def clicked():
    print("Combobox value:")
    print(combo.get())
    print("Radiobutton value:")
    print(selected.get())
    print("Checkbutton value:")
    print(chbselection.get())

def msgboxbotton():
    messagebox.showinfo('Message title', 'Message content')
    
btn1 = Button(window, text="Msg Box",command=msgboxbotton)
btn1.grid(column=0, row=3)

btn2 = Button(window, text="Print Values",command=clicked)
btn2.grid(column=1, row=3)
