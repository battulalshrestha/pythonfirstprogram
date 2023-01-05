
'''January - 31 days
February - 28 days in a common year and 29 days in leap years
March - 31 days
April - 30 days
May - 31 days
June - 30 days
July - 31 days
August - 31 days
September - 30 days
October - 31 days
November - 30 days
December - 31 days'''
from tkinter import *
fxn = Tk()
fxn. title("MONTH ICON BAR")
def Click():
 myfxn1 = Button(fxn,text = "january", padx = 3, pady = 4)
 myfxn1.grid()
 myfxn2 = Button(fxn,text = "February", padx = 3, pady = 6)
 myfxn2.grid()
 myfxn3 = Button(fxn,text = "March", padx = 3, pady = 8)
 myfxn3.grid()
 myfxn4 = Button(fxn,text = "April", padx = 3, pady = 10)
 myfxn4.grid()
 myfxn5 = Button(fxn,text = "May", padx = 3, pady = 12)
 myfxn5.grid()
 myfxn6 = Button(fxn,text = "June", padx = 3, pady = 14)
 myfxn6.grid()
 myfxn7 = Button(fxn,text = "July", padx = 3, pady = 16)
 myfxn7.grid()
 myfxn8 = Button(fxn,text = "August", padx = 3, pady = 18)
 myfxn8.grid()
 myfxn9 = Button(fxn, text = "September", padx=3, pady =20)
 myfxn9.grid()
 myfxn10 = Button(fxn,text = "October", padx = 3, pady = 22)
 myfxn10.grid()
 myfxn11 = Button(fxn,text = "November", padx = 3, pady = 24)
 myfxn11.grid()
 myfxn12 = Button(fxn,text = "December", padx = 3, pady = 26)
 myfxn12.grid()
my_fxn = Button(fxn, text = "click me", command=Click, padx = 27,pady = 25)
my_fxn.grid()
fxn.mainloop()
    
    