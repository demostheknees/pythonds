from pack.data_structures import Stack
import turtle
import random

class Tower(Stack, turtle.Turtle):

    def __init__(self, pos):
        Stack.__init__(self, name = pos)
        turtle.Turtle.__init__(self)

        if pos == "left":
            self.pos = -(x / 2)
        elif pos == "center":
            self.pos = 0
        elif pos == "right":
            self.pos = x / 2




class Disk(turtle.Turtle):

    colors = [0, "red", "green", "blue", "purple", "orange", "cyan", "pink"]

    def __init__(self, pos, start):
        self.pos = pos
        self.tower = start

        turtle.Turtle.__init__(self)
        self.color(self.colors[pos])
        self.resizemode("user")
        self.shape("square")
        self.shapesize(2 * pos, 1.5, 2)
        self.up()
        self.left(90)
        self.base = self.ycor()

        start.push(self)

        move_disk(self.tower, self.tower)



def move_tower(height, from_pole, to_pole, with_pole):

    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)

        move_disk(from_pole, to_pole)

        move_tower(height - 1, with_pole, to_pole, from_pole)


def move_disk(from_pole, to_pole):

    move = from_pole.pop()


    new_pos = to_pole.size()
    to_pole.push(move)

    move.pos = new_pos

    cur = move.ycor()
    move.sety((x - 100) - cur)
    move.setx(to_pole.pos)
    move.sety(move.base + (40 * move.pos))


wn = turtle.Screen()

x, y = 500, 500

wn.setworldcoordinates(-x, -y, x, y)

left = Tower("left")
center = Tower("center")
right = Tower("right")

# a = Disk(7, left)
# b = Disk(6, left)
# c = Disk(5, left)
# d = Disk(4, left)
e = Disk(3, left)
f = Disk(2, left)
g = Disk(1, left)

def main():

    move_tower(3, left, center, right)


wn.exitonclick()

