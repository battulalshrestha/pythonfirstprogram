
from tkinter import *
import random 
game_width = 800
game_height = 800
speed = 50
space_size = 50
body_parts = 3
snake_colour = '#00FF00'
food_colour = '#FF0000'
background_color = '#000000'
class Snake:
     pass
class Food:
    def __init__(self):
     x = random.randint(0,(game_width/space_size) - 1) *space_size
     y = random.randint(0,(game_height/space_size) - 1) *space_size
     self.axis = [x,y]
     canvas.create_oval(x,y,x+space_size,y+space_size,fill = food_colour,tag = "food")
def next_turn():
  pass
def change_diction(new_direction):
   pass
def cheak_collision():
  pass
def game_over():
 pass

nishan = Tk()
nishan.title("SNAKE GAME")
nishan.resizable(False,False)
score = 0
# direction = 'down'
mybutton  = Button(nishan, text = "Score:{}".format(score))
mybutton.grid()
canvas = Canvas(nishan, bg = background_color,height=game_height,width = game_width)
canvas.grid()
nishan.update()
mac_width  = nishan.winfo_width()
mac_height = nishan.winfo_height()
screen_width  =nishan.winfo_screenwidth()
screen_height = nishan.winfo_screenheight()
x = (screen_width/2) - (mac_width/2)
y = (screen_height/2) - (mac_width/2)
nishan.geometry(f"{mac_width}x{mac_height}+{x}+{y}")
snake = Snake()
nishan.mainloop()
