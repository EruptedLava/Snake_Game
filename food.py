from turtle import Turtle 
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()
        # rand_x = random.randint(-480,480)
        # rand_y = random.randint(-330,330)
        # self.goto(rand_x, rand_y)

    def refresh(self):
        rand_x = random.randint(-450,450)
        rand_y = random.randint(-300,300)
        self.goto(rand_x, rand_y)