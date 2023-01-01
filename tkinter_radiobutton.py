# we are going to make raidobutton so we can declear #radiobutton and it takes root,text as well as variable #little bit and value also as argument also to show on screen #can be grid() or pack()
# var is the text variable in tkinter here. so we can use boolen which return true or false called as booleanvar() fxn and it is upgraded the 0 and 1 return in programming
# Intvar i defined here because i can upgrade any integer value and from which it return a hole positive number
# strvar is a string variable text which update the string variable text 
# doublevar is also the double variable text which update double variable that why i already initialized it 
# get() fxn is also catch the fxn or it called the fxn 


from tkinter import *
main = Tk()
r= IntVar()
MODES = [ ("volume_high"),("volume_low"),("pause"),("play")]
intvar = IntVar()
strvar = StringVar()
boolvar = BooleanVar()
doublevar = DoubleVar()
left = StringVar()
left.set("volumn_high")
right = StringVar()
right.set("volume_low")
center = StringVar()
center.set("play")
back_center = StringVar()
back_center.set("pause")
main.title("Radio button")
intvar.set(100)
strvar.set("GFG")
boolvar.set(False)
doublevar.set(10.36)
def clicked(number):
   myButton = Button(main,text =number)
   myButton.grid()
Radiobutton(main,text = "option 1",variable = r, value = 1,command= lambda:clicked(left.get())).grid()
Radiobutton(main,text = "option 2",variable = r, value = 2,command= lambda:clicked(right.get())).grid()
Radiobutton(main,text = "option 3",variable = r, value = 3,command= lambda:clicked(center.get())).grid()
Radiobutton(main,text = "option 4",variable = r, value = 3,command= lambda:clicked(back_center.get())).grid()
myButton = Button(main, text ="Click me here!",command=clicked(left.get()))
myButton.grid()

  
main.mainloop()