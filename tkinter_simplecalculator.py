# This is an example of simple calculator of tkinter program. but it has not suitable row and column and space which can see on screen . it has also some bug
from tkinter import *
main = Tk()
main.title("simple calculator")
main.grid()
e = Entry(main, width = 35,borderwidth= 10,background="red")
e.grid(row= 0,column=0,columnspan=3,padx=10, pady= 10)
def button_click(number):
     current = e.get()
     e.delete(0,END)
     e.insert(0,str(current)+str(number))
def Button_clear():
  e.delete(0,END)
def Button_add():
  first_number = e.get()
  global f_num
  global math
  global second_number
  math = "addition"
  f_num = int(first_number)
  e.delete(0,END)
def Button_equal():
 second_number = e.get()
 e.delete(0,END)
 e.insert(0,f_num+int(second_number))
def button_minus():
 first_number = e.get()
 global f_num
 global math
 math = "subtraction"
 f_num = int(first_number)
 e.delete(0,END) 
def button_multiply():
  first_number = e.get()
  global f_num
  global math
  math = "multiply"
  f_num = int(first_number)
  e.delete(0,END)
def button_division():
  first_number = e.get()
  global f_num
  global math
  math = "division"
  f_num = int(first_number)
  e.delete(0,END)
  if math == "addition":
    e.insert(0,f_num+int(second_number))
  if math == "subtraction":
    e.insert(0,f_num+int(second_number))
  if math == "multiply":
    e.insert(0,f_num+int(second_number))
button_1= Button(main,text="1",padx= 40, pady =20, command=lambda:button_click(1))
button_2= Button(main,text="2",padx= 40, pady =20, command=lambda:button_click(2))
button_3= Button(main,text="3",padx= 40, pady =20, command=lambda:button_click(3))
button_4= Button(main,text="4",padx= 40, pady =20, command=lambda:button_click(4))
button_5= Button(main,text="5",padx= 40, pady =20, command=lambda:button_click(5))
button_6= Button(main,text="6",padx= 40, pady =20, command=lambda:button_click(6))
button_7= Button(main,text="7",padx= 40, pady =20, command=lambda:button_click(7))
button_8 = Button(main,text="8",padx= 40, pady =20, command=lambda:button_click(8))
button_9=Button(main,text="9",padx= 40, pady =20, command=lambda:button_click(9))
button_0= Button(main,text="0",padx= 40, pady =20, command=lambda:button_click(0))

button_add= Button(main,text="+",padx = 20,pady =32,command=lambda:button_click(0))
button_minus= Button(main,text="-",padx = 20,pady =32,command=lambda:button_click)
button_divide= Button(main,text="%",padx = 20,pady =32,command=lambda:button_click)
Button_clear =Button(main,text ="clear",padx=45, pady = 32,command =lambda:Button_clear)
button_equal = Button(main,text ="=", padx =43, pady =32,command=lambda:button_click)
button_multiply = Button(main,text ="*", padx =44, pady =32,command=lambda:button_click)


button_1.grid(row= 3,column=0 )
button_2.grid(row= 3,column=1 )
button_3.grid(row= 3,column= 2)

button_4.grid(row= 2,column= 0)
button_5.grid(row= 2,column= 1 )
button_6.grid(row= 2,column= 2)

button_7.grid(row= 1,column= 0)
button_8.grid(row= 1,column= 1)
button_9.grid(row= 1,column= 2 )

button_0.grid(row= 4,column= 0)
button_add.grid(row =4, column=1)
button_minus.grid(row =4, column=2)
button_divide.grid(row =5, column=1)
Button_clear.grid(row = 5,column=2)
button_equal.grid(row = 5,column=3)
button_multiply.grid(row =5 ,column =4)
main.mainloop()
