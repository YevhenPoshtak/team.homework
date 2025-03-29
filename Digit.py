import turtle
import math

class Digit:
    def __init__(self, value, angle, radius):
        self.value = value
        self.angle = angle
        self.radius = radius

    def draw(self, turtle_obj, offset_x=0, offset_y=-100):  # Додано зміщення
        x = self.radius * math.sin(math.radians(self.angle)) + offset_x
        y = self.radius * math.cos(math.radians(self.angle)) + offset_y - 15
        turtle_obj.penup()
        turtle_obj.goto(x, y)
        turtle_obj.pendown()
        turtle_obj.color("white")
        turtle_obj.write(str(self.value), align="center", font=("Comic Sans MS", 18, "bold"))

