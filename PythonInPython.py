import collections
from tkinter import *
from PIL import Image, ImageTk
import random
import pygame

class Snake:
    __slots__ = ( "direction", "x", "y")

    def __init__(self, direction = "right", x=4, y=7):
        self.direction = direction
        self.x = x 
        self.y = y
        
    
class Apple:
    __slots__ = ("x", "y", "is_spawn")
    def __init__(self, x=12, y=7, is_spawn=False):
        self.x = x
        self.y = y
        self.is_spawn = is_spawn
    
    def rollnums(self):
        self.x=random.randint(0,16)
        self.y=random.randint(0,14)

    
class pixel:
    __slots__ = ("x","y", "color")

    def __init__(self, y, x, color):
        self.y = y
        self.x = x
        self.color = color


def destroy_snakeLabel():
    for x in (snakelabel):
        x.after(1, x.destroy)
    snakelabel.clear()
        
def draw_snake():
    destroy_snakeLabel()
    for x in range(len(snakeBod)):
        p = (Label(root, image = redBsour))
        snakelabel.append(p)
        p.grid(row = snakeYs[x], column = snakeXs[x]) #add a snake y and a snake x after apple is eaten, only bod is being appened rn'
        p.grid()

    

def move(x_array, y_array):
    move_add()
    dequelisx = collections.deque(x_array)
    dequelisy = collections.deque(y_array)
    dequelisx.rotate(1)
    dequelisy.rotate(1)
    x_array = list(dequelisx)
    y_array = list(dequelisy)
    x_array[0] = head.x  #head is = to new x y
    y_array[0] = head.y 
    draw_snake()
    
    return x_array, y_array
    
def move_add():
    if head.direction == "right":
        head.x = head.x +1 
        print(head.x)
    elif head.direction =="up":
        head.y = head.y -1 
        print(head.y)   
    elif head.direction == "left":
        head.x = head.x -1 
        print(head.x)
    elif head.direction == "down":
        head.y = head.y +1
        print(head.y)
    
def dircU():
    if head.direction != "down":
        head.direction = "up"
        print(head.direction)
def dircR():
    if head.direction != "left":
        head.direction = "right"
        print(head.direction)
def dircD():
    if head.direction != "up":
        head.direction = "down"
        print(head.direction)
def dircL():
    if head.direction != "right":
        head.direction = "left"
        print(head.direction)

def apple_update():
    global apple_label

    if apple.is_spawn==False:
       for pixel in pixels:
           if pixel.x == apple.x and pixel.y == apple.y:
               apple_label = Label(root, image = applesour)
               apple_label.grid(row = pixel.y, column = pixel.x, columnspan=1, rowspan=1, pady= 0, padx=0)
               pixel.color = "red"
               apple.is_spawn=True     
               print(" apple_update")
               break
               
    if (snakeXs[0] == apple.x and snakeYs[0] == apple.y):
        snakeBod.append(Snake()) ##d
        apple.is_spawn == False
        apple_label.after(1, apple_label.destroy)
        print(" apple_update pos")               
        apple.rollnums()

    
root = Tk()
root.resizable(0,0)
root.title("PythonInPython")
root.iconbitmap('python32px.ico')

greenBsour = ImageTk.PhotoImage(Image.open("GreenBlock.jpg"))
redBsour = ImageTk.PhotoImage(Image.open("RedBlock.png"))
applesour = ImageTk.PhotoImage(Image.open("apple.png"))

root.bind("<w>", lambda event: dircU())
root.bind("<a>", lambda event: dircL())
root.bind("<s>", lambda event: dircD()) 
root.bind("<d>", lambda event: dircR())

gameon=True
apple = Apple()
head = Snake()

snakeXs = []
snakeYs = []
pixels = []
snakeBod = [] #holds snake object
snakelabel = [] #holds snake labels

start_clock = pygame.time.Clock()
if_clock = 0

for r in range(15):
    for c in range(17):
        pixels.append(pixel(r, c, "red"))
for pixel in pixels:
    Label(root, image = greenBsour).grid(row = pixel.y, column = pixel.x, columnspan=1, rowspan=1, pady= 0, padx=0)
    pixel.color = "green"

for c in range(3):
    snakeBod.append(Snake())
    snakeXs.append(4-c)
    snakeYs.append(7)


while gameon == True:
    snakeXs, snakeYs = move(snakeXs, snakeYs)
    print(snakeXs, snakeYs, len(snakeBod), len(snakelabel))  #fix itteration with direction adn apple spawning/destroyiong
    apple_update()
    root.update()
    start_clock.tick(3)

