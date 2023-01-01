from tkinter import *
top = Tk()
# i made a double click me on the screen .when i click one "click me" button then it call its function from which its commend
def myClick():
  myButton = Button(top, text= "welcome to my machine!:",padx= 34, pady= 45,command= afterClick)
  myButton.grid()
def afterClick():
  myButton = Button(top,text ="you can see me!",padx = 43)
  myButton.grid()

myButton = Button(top,text = "click me!",command= myClick)
myButton.grid()
myButton = Button(top,text = "click me!",command= afterClick)
myButton.grid()
top.mainloop()