import turtle
import time
import random
from Watch import Watch


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
        self.pen.color("black")
        self.pen.write(time_str, align="center", font=("Comic Sans MS", 24, "bold"))

        if self.alarm_time and time.strftime("%H:%M:%S", self.current_time) == self.alarm_time:
            self.pen.goto(0, -280)
            self.pen.color("red")
            self.pen.write("Час прокидатися!", align="center", font=("Arial", 16, "bold"))
            self.pen.goto(0, -250)
        turtle.update()


if __name__ == '__main__':
    D_watch = DigitalWatch(alarm_time="02:11:00")
    D_watch.start()
    turtle.mainloop()