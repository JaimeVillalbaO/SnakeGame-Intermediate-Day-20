from turtle import Turtle, colormode
import random

colormode(255)

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.speed('fastest')
        self.refresh()
        
        

    def refresh(self):       
         
        self_r = random.randint(0, 255)
        self_g = random.randint(0, 255)
        self_b = random.randint(0, 255)
        self_tuple = (self_r, self_g, self_b)      
        self.color(self_tuple)

        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)  
        self.goto(random_x, random_y)
