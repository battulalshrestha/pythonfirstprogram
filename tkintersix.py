import os
TK_SILENCE_DEPRECATION = "1"
from tkinter import *
main  = Tk()
main.title("welcome to nishan")
def click():
   myButton = Button(main, text =['sunday','monday','tuesday','wedneday','thrusday','friday','saturday'],padx= 20, pady = 13)
   myButton.grid()
myScreen = Button(main, text = "click here",command=click)
myScreen.grid()
main.mainloop()