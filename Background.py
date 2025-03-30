import turtle
import random

turtle.setup(700, 700)
turtle.tracer(0)
screen = turtle.Screen()
list_stars = []

for _ in range(20):
    x = random.randint(-350, 350)
    y = random.randint(-350, 350)
    list_stars.append((x, y))


class Background:
    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.hideturtle()

    def draw(self, hour):
        self.pen.clear()
        if 6 <= hour < 18:
            screen.bgcolor("sky blue")
            self.pen.up()
            self.pen.goto(200, -200)
            self.pen.dot(50, 'yellow')
            self.pen.dot(25, 'orange')
        else:
            screen.bgcolor("midnight blue")
            for el in list_stars:
                self.pen.penup()
                self.pen.goto(*el)
                self.pen.dot(random.randint(2, 5), "white")
                self.pen.goto(200, -200)
                self.pen.dot(50, 'white')
                self.pen.goto(220, -200)
                self.pen.dot(50, 'midnight blue')


if __name__ == '__main__':
    background = Background()
    background.draw(11)
    turtle.mainloop()
