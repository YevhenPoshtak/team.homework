import turtle
import time


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
