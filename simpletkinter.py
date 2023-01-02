from tkinter import *
main = Tk()
var =IntVar()
def click():
      myButton= Button(main,text =var.get())
      myButton.grid()
c = Checkbutton(main,text ="food",variable=var,value = None)
c.grid()
main.mainloop()