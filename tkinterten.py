from tkinter import *
main = Tk()
main.title("nishan icon")
def Click():
 myButton1 = Button(main, text = "hi nishan",padx = 20 ,pady =23, bg= "white",background='red')
 myButton1.grid()
myButton1 = Button(main, text = "click here",command=Click, padx = 12,pady =13)
myButton1.grid()
def Click1():
  myButton2 = Button(main, text ="hello again",padx = 29,pady= 23)
  myButton2.grid()
myButton2 = Button(main,text = "click me again",command=Click1,padx = 23, pady=25)
myButton2.grid()
main.mainloop()