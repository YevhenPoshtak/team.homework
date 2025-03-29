import turtle
import time
import math
import random

class Hand:
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color
        self.angle = 0

    def set_angle(self, angle):
        self.angle = angle

    def draw(self, turtle_obj, offset_x=0, offset_y=120):
        turtle_obj.penup()
        turtle_obj.goto(offset_x, offset_y)
        turtle_obj.setheading(self.angle)
        turtle_obj.pensize(self.width)
        turtle_obj.color(self.color)
        turtle_obj.pendown()
        turtle_obj.forward(self.length)
        x = self.length * math.sin(math.radians(self.angle)) + offset_x
        y = self.length * math.cos(math.radians(self.angle)) + offset_y
        turtle_obj.penup()
        turtle_obj.goto(x, y)
        turtle_obj.dot(self.width * 3, self.color)
