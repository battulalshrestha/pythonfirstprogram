

from tkinter import *
main = Tk()
x1 =0
width = 900
height = 700
step = 5
c_width = width-10
c_height = height-65
d = str(width)+"x"+str(height)
main.geometry(d)


canvas = Canvas(main,width = c_width,height = c_height)
canvas.grid(row=0, column=0,padx = 5,pady=5)
x1 ,y1 = 5,int(c_height/2)
x2 = x1+15
y2 = y1+15

canvas.grid()
# making line on canvas
r = canvas.create_rectangle(x1,y1,x2,y2,fill = "blue")
#to create a canvas we have to fill the x1,y1,x2,y2 co-ordinates
def my_draw():
    global x1,y1,x2,y2,r
    canvas.delete(r)
    r=canvas.create_rectangle(x1,y1,x2,y2,fill = "blue")
    if(x2<(c_width-step)):
#moving canvas for the right movement 
     x1 = x1+step
     x2 = x2+step
     canvas.after(100,my_draw)
    else:
       return
my_draw()
def Click():
  global x1,y1,x2,y2,r
  x1 ,y1 = 5,int(c_height/2)
  x2 = x1+15
  y2 = y1+15
myButton = Button(main, text = "Restart", command=Click)
myButton.grid()
main.mainloop()
# running the main loop
