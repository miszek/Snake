from turtle import Screen, Turtle
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
    snake.move()
    screen.update()


screen.exitonclick()
