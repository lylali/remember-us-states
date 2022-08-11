from turtle import Turtle
import time

class Screenwrite(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_text(self, text):
        self.goto(0, 0)
        self.write(text, False, "center", ('Courier', 20, 'bold'))
        time.sleep(1)
        self.clear()
