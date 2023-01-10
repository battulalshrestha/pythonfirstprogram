
# importing whole module

from tkinter import *
 
# importing strftime function to
# retrieve system's time
from time import strftime
 
# creating tkinter window
main = Tk()
main.title('digital clock')
 
# This function is used to
# display time on the Button 
 
def time():
    string = strftime('%H:%M:%S %p')
    Button.config(text=string)
    Button.after(1000, time)
 
 
# Styling the label widget so that clock
# will look more attractive
myButton= Button(main, font=('calibri', 100, 'bold'),
            background='purple',
            foreground='white')
myButton.grid()
 
# Placing clock at the centre
# of the tkinter window
myButton=Button(main,padx =23,pady =25)
myButton.grid()
 
main.mainloop()