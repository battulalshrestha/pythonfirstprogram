# Its a extra level of rocket launch program ,it show rocket launch on screen then you said "yes" then it will launch but when you said "no"then it return back and didnot lauch
from tkinter  import *
from tkinter import messagebox
main = Tk()
main.title("nishan messege box")
def rocket():
   response=messagebox.askyesno("its my rocket","rocket is ready to lauch!")
   Button(main,text = response).grid()
   if response == 1:
      Button(main,text ="you said yes!").grid()
   elif(response == 2):
        Button(main,text = "you said nothing try again please!").grid()
   else:
        Button(main,text = "you said no!").grid()
                      
Button(main, text = "rocket",command= rocket).pack()
main.mainloop()