# here i also just made two function to call in to the screen

from tkinter import *
main = Tk()
main.title("Screen icon")
e = Entry(main, width = 35,borderwidth= 10,background="red")
e.grid(row= 0,column=0,columnspan=3,padx=10, pady= 10)
str = StringVar
int = IntVar
global vars
def Click():
    myButton = Button(main, text = "year",padx = 20 , pady = 13)
    myButton.grid()
def firstmonth():
    myButton = Button(main, text = "baisakh",padx = 20 , pady = 13)
    myButton.grid()

myButton = Button(main,text = "click here", command= Click,padx = 12,pady= 13)
myButton.grid()
myButton = Button(main,text = "click agian", command=firstmonth,padx = 12, pady = 15)
myButton.grid()
myButton.grid()
main.mainloop()
