import turtle
import time
import math
import random
from Background import Background
from Dial import Dial
from Hand import Hand
from Watch import Watch
from AnalogWatch import AnalogWatch

class DigitalWatch(Watch):
    def __init__(self, format='24h', alarm_time=None):
        super().__init__()
        self.format = format
        self.alarm_time = alarm_time
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.goto(0, -250)

    def display(self):
        self.pen.clear()
        if self.format == '24h':
            time_str = time.strftime("%H:%M:%S", self.current_time)
        elif self.format == '12h':
            time_str = time.strftime("%I:%M:%S %p", self.current_time)
        else:
            raise ValueError("Invalid format")
        self.pen.color("white")
        self.pen.write(time_str, align="center", font=("Comic Sans MS", 24, "bold"))

        if self.alarm_time and time.strftime("%H:%M:%S", self.current_time) == self.alarm_time:
            self.pen.goto(0, -280)
            self.pen.color("red")
            self.pen.write("Час прокидатися!", align="center", font=("Arial", 16, "bold"))
            for _ in range(5):
                self.pen.penup()
                self.pen.goto(random.randint(-50, 50), random.randint(-300, -260))
                self.pen.dot(5, "yellow")

        turtle.update()
