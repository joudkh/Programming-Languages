import tkinter
flag = 0

def updateDisplay():
    global flag
    if flag == 1:
        flag=0
        catPic.config(image = firstphoto)
    else:
        flag=1
        catPic.config(image = secondphoto)
        
root = tkinter.Tk()
root.geometry("500x300")

firstphoto = tkinter.PhotoImage(file="1.gif")
secondphoto = tkinter.PhotoImage(file="2.gif")

catPic = tkinter.Label(root, image=firstphoto)
catPic.place(x=100,y=0)
btnFeed = tkinter.Button(root, text="Click Me", command=updateDisplay)
btnFeed.place(x=200,y=200)
