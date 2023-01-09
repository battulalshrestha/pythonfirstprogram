from tkinter import *


# Create the root window
main = Tk()

# Create a widget and set its size and position using the .geometry() method
main.geometry("800x600+100+100")
myButton = Button(main,text = "Nishan")
myButton.grid()
# Run the Tkinter event loop
main.mainloop()