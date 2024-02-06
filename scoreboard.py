from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(x=0, y=260)
        self.hideturtle()
        self.print_score()

    def increase_score(self):
        self.score += 1
        self.print_score()

    def print_score(self):
        self.clear()
        writing = "Score: " + str(self.score)
        self.write(writing, align="center", font=('Arial', 24, 'normal'))
