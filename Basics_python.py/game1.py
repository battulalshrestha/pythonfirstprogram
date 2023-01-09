# key x1  = left, x2 = right , y1 = up , y2 = down

from tkinter import *
main = Tk()
# i give the tkinter window length and height of the window in th screen
width = 900
height = 700
# the step is nothing. its just the the speed or moving step of the canvas food on the screen
step = 10
# the two width and height define the canvas width and height on the screen in which canvas moves in x and y direction 
c_width = width-10
c_height = height-65
# i intialize the geometry of the canvas height and width in the screen thats why i make the area of the canvas . and called as the canvas widgets   
d = str(width)+"x"+str(height)
#
main.geometry(d)


canvas = Canvas(main,width = c_width,height = c_height)
canvas.grid(row=0, column=0,padx = 5,pady=5,columnspan=3)
x1 ,y1 = 5 ,int(c_height/2)#5
x2 = x1+15 #15
y2 = y1+15

canvas.grid()
# making line on canvas
r = canvas.create_rectangle(x1,y1,x2,y2,fill = "blue")
#to create a canvas we have to fill the x1,y1,x2,y2 co-ordinates
def right(event):
# collecting globel variable and decleared value
    global x1,y1,x2,y2,r
    if(x2<(c_width-step)):
#moving canvas for the right movement 
     x1 = x1+step
     x2 = x2+step
     canvas.delete(r)
     r=canvas.create_rectangle(x1,y1,x2,y2,fill = "blue")
def left(event):
# collecting globel variable and decleared value
    global x1,y1,x2,y2,r
    if(x1>(step)):
#moving canvas for the right movement 
     x1 = x1-step
     x2 = x2-step
     canvas.delete(r)
     r=canvas.create_rectangle(x1,y1,x2,y2,fill = "blue")
def up(event):
# collecting globel variable and decleared value
    global x1,y1,x2,y2,r
    if(y1>(step)):
#moving canvas for the right movement 
     y1 = y1-step
     y2 = y2-step
     canvas.delete(r)
     r=canvas.create_rectangle(x1,y1,x2,y2,fill = "blue")

def down(event):
# collecting globel variable and decleared value
    global x1,y1,x2,y2,r
    if(y2<(c_height-step)):
#moving canvas for the right movement 
     y1= y1+step
     y2 = y2+step
     canvas.delete(r)
     r=canvas.create_rectangle(x1,y1,x2,y2,fill = "blue")

myButton1 = Button(main,text = "Left",command=lambda:left('x'))
myButton1.grid(row =1,column=0)
myButton2 = Button(main,text = "Right",command=lambda:right('x'))
myButton2.grid(row =1,column=1)
myButton3 = Button(main,text = "Up",command=lambda:up('x'))
myButton3.grid(row =1,column=2)
myButton4= Button(main,text = "Down",command=lambda:down('x'))
myButton4.grid(row =1,column=3)


main.mainloop()










'''def Pause(): 
  global x1,y1,x2,y2,r
  x1 ,y1 = 5,int(c_height/2)
  x2 = x1+15
  y2 = y1+15
myButton1 = Button(main,text= "play",command=lambda:Pause())
myButton1.grid(row=1,column=1)
my_draw()

def my_drawy():
    global x1,y1,x2,y2,r
    canvas.delete(r)
    r=canvas.create_rectangle(x1,y1,x2,y2,fill = "blue")
    if(y2<(c_height)):
#moving canvas for the right movement 
     y1 = y1+step
     y2 = y2+step
     canvas.after(100,my_drawy)
    else:
       return
my_drawy()
main.mainloop()'''