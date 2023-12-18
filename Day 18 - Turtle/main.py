from turtle import Turtle, Screen
from random import choice

tim = Turtle()
tim.shape("turtle")
tim.color("cyan1")


def random_walk():
    colors = [
        "red", "green", "blue", "orange", "purple",
        "pink", "yellow", "brown", "black", "white",
        "gray", "cyan", "magenta", "lightgreen", "darkgreen",
        "navy", "skyblue", "turquoise", "lightpink", "darkred",
        "gold", "violet", "darkblue", "lightblue", "lime",
        "chocolate", "coral", "beige", "mintcream", "aliceblue"
    ]

    directions = [0, 90, 180, 270]
    tim.pensize(5)
    tim.speed("fastest")

    for _ in range(200):
        tim.color(choice(colors))
        tim.forward(30)
        tim.setheading(choice(directions))

random_walk()
