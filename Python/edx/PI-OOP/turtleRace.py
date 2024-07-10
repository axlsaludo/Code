from turtleNames import TurtleNames
from random import randint
from turtle import Screen

screen = Screen()
screen.title("Turtles Race")
screen.bgcolor("black")


# Create turtle instances from the turtle names module

laura = TurtleNames("Laura", "red")
rik = TurtleNames("Rik", "blue")
lauren = TurtleNames("Lauren", "green")
carrieann = TurtleNames("Carrieann", "pink")

laura.goto(-160, 100)
rik.goto(-160, 70)
lauren.goto(-160, 40)
carrieann.goto(-160, 10)

# Race logic
for movement in range(100):
    laura.forward(randint(1, 5))
    rik.forward(randint(1, 5))
    lauren.forward(randint(1, 5))
    carrieann.forward(randint(1, 5))

screen.mainloop()
