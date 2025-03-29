import turtle
import time
import math
import random
from Digit import Digit


class Dial:
    def __init__(self, radius):
        self.radius = radius
        self.digits = []
        self.stars = []

        for i in range(1, 13):
            angle = (12 - i) * 30
            angle %= 360
            if i not in [12, 6]:
                angle = (360 - angle) % 360
            digit = Digit(i, angle, radius)
            self.digits.append(digit)

        for _ in range(12):
            angle = random.uniform(0, 360)
            x = (self.radius + 20) * math.cos(math.radians(angle))
            y = (self.radius + 20) * math.sin(math.radians(angle))
            self.stars.append((x, y))

    def draw(self, turtle_obj, offset_x=0, offset_y= 120):
        turtle_obj.penup()
        turtle_obj.goto(offset_x + self.radius, offset_y - self.radius/2 )
        turtle_obj.pendown()
        turtle_obj.pensize(8)
        turtle_obj.color("gold")
        turtle_obj.circle(self.radius)

        for x, y in self.stars:
            turtle_obj.penup()
            turtle_obj.goto(x + offset_x, y + offset_y)
            turtle_obj.dot(3, "yellow")

        for digit in self.digits:
            digit.draw(turtle_obj, offset_x, offset_y)
