import turtle
import time
import math
import random
from Background import Background
from Dial import Dial
from Hand import Hand
from Watch import Watch
from AnalogWatch import AnalogWatch
from DigitalWatch import DigitalWatch


def toggle_format():
    digital_watch.format = '24h' if digital_watch.format == '12h' else '12h'


if __name__ == "__main__":
    analog_watch = AnalogWatch(200)
    digital_watch = DigitalWatch('12h', alarm_time="11:45:40")

    analog_watch.start()
    digital_watch.start()

    turtle.listen()
    turtle.onkey(toggle_format, "space")
    turtle.mainloop()
