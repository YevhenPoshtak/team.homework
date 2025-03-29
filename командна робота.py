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
            for _ in range(20):
                self.pen.penup()
                self.pen.goto(random.randint(-250, 250), random.randint(-250, 250))
                self.pen.dot(random.randint(2, 5), "white")


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
        turtle_obj.goto(offset_x, -self.radius + offset_y)
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


class Watch:
    def __init__(self):
        self.current_time = None

    def update(self):
        self.current_time = time.localtime()

    def display(self):
        raise NotImplementedError

    def start(self, interval=1000):
        def timer_func():
            self.update()
            self.display()
            turtle.ontimer(timer_func, interval)

        timer_func()


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


if __name__ == "__main__":
    analog_watch = AnalogWatch(200)
    digital_watch = DigitalWatch('12h', alarm_time="11:45:40")

    analog_watch.start()
    digital_watch.start()

    def toggle_format():
        digital_watch.format = '24h' if digital_watch.format == '12h' else '12h'

    turtle.listen()
    turtle.onkey(toggle_format, "space")
    turtle.mainloop()
