from tkinter import *
name = Tk()
def click():
 mybutton  =Button(name, text = "enter my name")
 mybutton.grid()
mybutton1 = Button(name, text ="shyam",command=click)
mybutton1.grid()


name. mainloop()
