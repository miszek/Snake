from turtle import Turtle


class Snake:
    positions = [(-40, 0), (-20, 0), (0, 0)]

    def __init__(self):
        for position in self.positions:
            turtle = Turtle()
            turtle.shape('square')
            turtle.color('white')
            turtle.penup()
            turtle.goto(position[0], position[1])