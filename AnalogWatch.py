import turtle
from Background import Background
from Dial import Dial
from Hand import Hand
from Watch import Watch


class AnalogWatch(Watch):
    def __init__(self, radius):
        super().__init__()
        self.dial = Dial(radius)
        self.second_hand = Hand(radius * 7/8, 1, "red")
        self.minute_hand = Hand(radius * 2/3, 3, "blue")
        self.hour_hand = Hand(radius//2, 5, "green")
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.hideturtle()
        self.background = Background()
        self.offset_x = 0
        self.offset_y = 100


    def display(self):
        self.pen.clear()
        self.background.draw(self.current_time.tm_hour)
        self.pen.setheading(0)
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

        turtle.update()


if __name__ == '__main__':
    analog_watch = AnalogWatch(200)
    analog_watch.start()
    turtle.mainloop()
