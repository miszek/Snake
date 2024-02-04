from turtle import Turtle
import time


def create_turtle(pos_x, pos_y):
    turtle = Turtle()
    turtle.penup()
    turtle.shape('square')
    turtle.color('white')
    turtle.setx(pos_x)
    turtle.sety(pos_y)
    return turtle


class Snake:
    turtles = []
    direction = 0

    def __init__(self):
        initial_positions = [(-40, 0), (-20, 0), (0, 0)]
        for position in initial_positions:
            pos_x = position[0]
            pos_y = position[1]
            self.turtles.append(create_turtle(pos_x, pos_y))

    def move(self):
        head_turtle = self.turtles[len(self.turtles) - 1]
        head_turtle_pos_x = head_turtle.position()[0]
        head_turtle_pos_y = head_turtle.position()[1]

        if self.direction == 0:
            head_turtle_pos_x += 20
        elif self.direction == 90:
            head_turtle_pos_y += 20
        elif self.direction == 180:
            head_turtle_pos_x -= 20
        elif self.direction == 270:
            head_turtle_pos_y -= 20

        for i in range(0, len(self.turtles) - 1):
            current_turtle = self.turtles[i]
            next_turtle = self.turtles[i + 1]
            current_turtle.setx(next_turtle.xcor())
            current_turtle.sety(next_turtle.ycor())
        head_turtle.setx(head_turtle_pos_x)
        head_turtle.sety(head_turtle_pos_y)

        time.sleep(0.2)