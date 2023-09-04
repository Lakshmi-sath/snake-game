from turtle import Turtle
import random

# random_shapes = random.choice(["circle", "triangle", "square"])
random_colors = random.choice(["red", "blue", "#EC53B0", "light pink", "orange", "brown", "black"])


class Food(Turtle):

    def __init__(self):

        super().__init__()
        self.color(random_colors)
        self.shape("circle")
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
