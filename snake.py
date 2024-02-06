from turtle import Turtle
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


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
    direction = RIGHT

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

        if self.direction == RIGHT:
            head_turtle_pos_x += 20
        elif self.direction == UP:
            head_turtle_pos_y += 20
        elif self.direction == LEFT:
            head_turtle_pos_x -= 20
        elif self.direction == DOWN:
            head_turtle_pos_y -= 20

        for i in range(0, len(self.turtles) - 1):
            current_turtle = self.turtles[i]
            next_turtle = self.turtles[i + 1]
            current_turtle.setx(next_turtle.xcor())
            current_turtle.sety(next_turtle.ycor())
        head_turtle.setx(head_turtle_pos_x)
        head_turtle.sety(head_turtle_pos_y)

        time.sleep(0.1)

    def up(self):
        if self.direction != DOWN:
            self.direction = UP

    def down(self):
        if self.direction != UP:
            self.direction = DOWN

    def left(self):
        if self.direction != RIGHT:
            self.direction = LEFT

    def right(self):
        if self.direction != LEFT:
            self.direction = RIGHT

    def get_head(self):
        return self.turtles[-1]

    def is_collision(self):
        head = self.get_head()
        if head.xcor() < -280 or head.xcor() > 280 or head.ycor() < -280 or head.ycor() > 280:
            return True
