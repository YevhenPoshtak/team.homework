import turtle
import math
import random
from Digit import Digit


class Dial:
    def __init__(self, radius):
        self.radius = radius
        self.digits = []

        for i in range(1, 13):
            angle = (12 - i) * 30
            angle %= 360
            if i not in [12, 6]:
                angle = (360 - angle) % 360
            digit = Digit(i, angle, radius + 20)
            self.digits.append(digit)


    def draw(self, turtle_obj, offset_x=0, offset_y=0):
        turtle_obj.penup()
        turtle_obj.goto(offset_x, offset_y - self.radius)
        turtle_obj.pendown()
        turtle_obj.pensize(8)
        turtle_obj.color("gold")
        turtle_obj.circle(self.radius)

        for digit in self.digits:
            digit.draw(turtle_obj, offset_x, offset_y)


if __name__ == '__main__':
    pen = turtle.Turtle()
    screen = turtle.Screen()
    screen.bgcolor("sky blue")

    dial = Dial(90)
    dial.draw(pen, 0, 0)
    turtle.mainloop()
