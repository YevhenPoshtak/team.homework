import turtle
import time
import math
import random
from Background import Background
from Dial import Dial
from Hand import Hand
from Watch import Watch


class AnalogWatch(Watch):
    def __init__(self, radius):
        super().__init__()
        self.dial = Dial(radius)
        self.second_hand = Hand(180, 1, "red")
        self.minute_hand = Hand(150, 3, "blue")
        self.hour_hand = Hand(100, 5, "green")
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.hideturtle()
        self.background = Background()
        self.offset_x = 0
        self.offset_y = 120

    def display(self):
        self.pen.clear()
        self.background.draw(self.current_time.tm_hour)
        self.dial.draw(self.pen, self.offset_x, self.offset_y)

        seconds = self.current_time.tm_sec
        minutes = self.current_time.tm_min
        hours = self.current_time.tm_hour

        second_angle = (90 - seconds * 6) % 360
        minute_angle = (90 - (minutes + seconds / 60) * 6) % 360
        hour_angle = (90 - (hours % 12 + minutes / 60 + seconds / 3600) * 30) % 360

        self.second_hand.set_angle(second_angle)
        self.minute_hand.set_angle(minute_angle)
        self.hour_hand.set_angle(hour_angle)

        self.second_hand.draw(self.pen, self.offset_x, self.offset_y)
        self.minute_hand.draw(self.pen, self.offset_x, self.offset_y)
        self.hour_hand.draw(self.pen, self.offset_x, self.offset_y)

        if seconds == 0:
            self.pen.penup()
            self.pen.goto(self.offset_x, self.offset_y)
            self.pen.color("yellow")
            self.pen.dot(20)
        turtle.update()
