import turtle
import random

hilbert = turtle.Turtle()
hilbert.speed("fastest")
hilbert.pensize("3")

space = turtle.Screen()



def curve(turtle, size, angle, order):

    selector = []
    for i in range(order + 1, 0, -1):
        selector.append(i)

    h_line = "--- " * selector[order]
    indent = " " * selector[order]

    colors = ["red", "green", "blue"]

    if order == 0:
        pass

    else:

        turtle.color(random.choice(colors))

        print(h_line, "Curve Start |", "Color:", turtle.pencolor(), "|", "Order:", order, h_line, "\n")

        turtle.right(angle)
        print(indent, "turning", angle, "degrees","\n")


        curve(turtle, size, -angle, order - 1)
        print("1st Recursive Call", "Order is", order, "\n")


        turtle.forward(size)
        print(indent, "going forward", size, "\n")

        turtle.left(angle)
        print(indent, "turning", angle, "degrees", "\n")

        curve(turtle, size, angle, order - 1)
        print("2nd Recursive Call", "Order is", order, "\n")


        turtle.forward(size)
        print(indent, "going forward", size, "\n")

        curve(turtle, size, angle, order - 1)
        print("3rd Recursive Call", "Order is", order, "\n")

        turtle.left(angle)
        print(indent, "turning", angle, "degrees", "\n")

        turtle.forward(size)
        print(indent, "going forward", size, "\n")

        curve(turtle, size, -angle, order - 1)
        print("4th Recursive Call", "Order is", order, "\n")


        turtle.right(angle)
        print(indent, "turning", angle, "degrees", "\n")

        print(h_line, "Curve End", h_line, "\n")


        turtle.color("black")



def main():

    curve(hilbert, 10, 90 , 40)

    space.exitonclick()