# you can concaninate with text that you entry in screen with Entry function 
from tkinter import *
main = Tk()
e= Entry(main,width=45)
e.pack()
def myclick():
    myButton = Button(main,text = "hello nishan!" +e.get())
    myButton.pack()
mynishan = Button(main, text ="welcome to the nishan machine:",command = myclick)
mynishan.pack()
main.mainloop()