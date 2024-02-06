from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(x=0, y=260)
        self.hideturtle()
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        writing = "Score: " + str(self.score)
        self.write(writing, align="center", font=('Arial', 24, 'normal'))
