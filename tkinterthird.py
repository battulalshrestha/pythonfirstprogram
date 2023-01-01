from tkinter import *
main = Tk()
# i make function to give instruction, it seen button as click me on screen when i click "click me" it click as functiom myClick and open as myClick function and open as "see . i just click " on the screen due to function call
def myClick(): 
   myButton = Button(main,text = "see . i just click",padx= 34, pady =45)
   myButton.grid()
myButton =Button(main, text = "click me !",command= myClick)
myButton.grid()
main.mainloop()