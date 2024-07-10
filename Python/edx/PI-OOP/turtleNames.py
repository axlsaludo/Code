from turtle import Turtle

class TurtleNames(Turtle):
    def __init__(self, name, color):
        super().__init__()
        self.name = name
        self.color(color)
        self.shape("turtle")
        self.penup()
        self.goto(-160, 100)
        self.pendown()

class TurtleShapes:
    def __init__(self, turtle, shape):
        self.turtle = turtle
        self.shape = shape
        self.turtle.shape(self.shape)
