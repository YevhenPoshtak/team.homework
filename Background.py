import turtle
import time
import math
import random

turtle.setup(500, 500)
turtle.tracer(0)
screen = turtle.Screen()


class Background:

    def __init__(self):

        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.hideturtle()

    def draw(self, hour):
        self.pen.clear()
        if 6 <= hour < 18:
            screen.bgcolor("sky blue")
        else:
            screen.bgcolor("midnight blue")
            for _ in range(10):
                self.pen.penup()
                self.pen.goto(random.randint(-250, 250), random.randint(-250, 250))
                self.pen.dot(random.randint(2, 5), "white")
