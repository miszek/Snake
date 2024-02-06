import random
from turtle import Turtle
from random import Random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('pink')
        self.speed('fastest')
        self.refresh()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)

    def refresh(self):
        pos_x = random.randint(-280, 280)
        pos_y = random.randint(-280, 280)
        self.goto(pos_x, pos_y)