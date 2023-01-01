from tkinter import *
nishan = Tk()
myButton1 = Button(nishan, text ="welcome to the nishan machine",padx = 45,pady = 67)
myButton2 = Button(nishan, text = " enter your email or phonenumber:", padx = 23, pady =34)
myButton3 = Button(nishan,text = "enter your password:", padx = 30, pady = 45)
myButton1.grid()

myButton2.grid()
myButton3.grid()
nishan.mainloop()
