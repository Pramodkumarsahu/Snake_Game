import turtle
import random
import time

screen = turtle.Screen()
screen.title('DATAFLAIR SNAKE GAME')
screen.setup(width = 700, height = 700)
screen.tracer(0)
turtle.bgcolor('turquoise')

turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color('black')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()