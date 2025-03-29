import turtle
import math


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



if __name__ == '__main__':
    second_hand = Hand(180, 1, "red")
    minute_hand = Hand(150, 3, "blue")
    hour_hand = Hand(100, 5, "green")

    pen = turtle.Turtle()

    seconds = 20
    minutes = 40
    hours = 2

    second_angle = (90 - seconds * 6) % 360
    minute_angle = (90 - (minutes + seconds / 60) * 6) % 360
    hour_angle = (90 - (hours % 12 + minutes / 60 + seconds / 3600) * 30) % 360

    second_hand.set_angle(second_angle)
    minute_hand.set_angle(minute_angle)
    hour_hand.set_angle(hour_angle)

    second_hand.draw(pen, 0, 0)
    minute_hand.draw(pen, 0, 0)
    hour_hand.draw(pen, 0, 0)
    turtle.mainloop()