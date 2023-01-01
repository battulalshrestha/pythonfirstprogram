# Its a python rocket program when you give comment then it will ready for launch
from tkinter  import *
from tkinter import messagebox
main = Tk()
main.title("Nepali rocket")
def rocket():
   messagebox.showinfo("its my rocket","rocket is ready to lauch!")
Button(main, text = "rocket",command= rocket).pack()
main.mainloop()