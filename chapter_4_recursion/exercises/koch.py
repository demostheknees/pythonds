import turtle
import random




def koch(t, length, angles, order):

    if order == 0:

        t.forward(length)

    else:
        for angle in angles:
            koch(t, length / 3, angles, order - 1)
            t.left(angle)



def draw_snowflake(t, length, order):

    x_one = random.uniform(50,80)
    x_two = random.uniform(50,80)
    x_three = -(x_one + x_two)

    rand_angles = [x_one, x_three, x_two, 0]

    eq_angles = [60, -120, 60, 0]

    for side in range(3):
        koch(t, length, eq_angles, order)
        t.right(120)



def setup(t, x_cor, y_cor):

    t.up()

    t.setpos(x_cor, y_cor)

    t.down()


def main():

    frosty = turtle.Turtle()

    frosty.speed("fastest")

    wn = turtle.Screen()

    x, y = 500, 500

    flake_size = x

    centered = flake_size / 2

    wn.setworldcoordinates(-x, -y, x, y)

    setup(frosty, -centered, centered)

    wn.tracer(0,0)

    draw_snowflake(frosty, flake_size, 3)

    wn.update()

    wn.exitonclick()


main()

