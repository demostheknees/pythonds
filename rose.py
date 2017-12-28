import turtle
import random



gaia = turtle.Turtle()
gaia.speed("slowest")

wn = turtle.Screen()

x,y = 400, 400

wn.setworldcoordinates(-x, -y, x, y)

wn.bgcolor("#D9B9B9")





def make_wrap(t, length, width, color, peak):

    t.color(color)

    t.up()


    t.backward(10)

    x1 = t.pos()

    t.forward(length)

    x2 = t.pos()

    t.backward(length / peak)

    t.right(90)
    t.forward(width / 2)

    y1 = t.pos()

    t.left(180)
    t.forward(width)

    y2 = t.pos()

    t.goto(x1)
    t.down()

    t.begin_fill()
    t.goto(y1)
    t.goto(x2)
    t.goto(y2)
    t.goto(x1)
    t.end_fill()

    t.right(90)

def draw_stem(t, length, angle):
    t.forward(length)
    t.right(angle)


def draw_bulbs(t, colors):
    t.up()
    t.resizemode("user")
    t.shapesize(2.75, 2.75)
    t.color(random.choice(colors))
    t.tilt(180)
    t.stamp()
    t.tilt(180)
    t.resizemode("auto")
    t.color(random.choice(colors))


def draw_roses(t, length, min_angle, max_angle, min_shrink, max_shrink, thickness):

    t.pensize(thickness)

    petal_colors = ["#b20000","#cc0000", "#990000"]
    stem_colors = ["#007300", "#006600", "#008000"]

    if length > 10:
        t.color(random.choice(stem_colors))

    else:
        draw_bulbs(t, petal_colors)


    angle1 = random.uniform(min_angle, max_angle)

    shrink1 = random.uniform(min_shrink, max_shrink)
    shrink2 = random.uniform(min_shrink, max_shrink)

    if length > 10:


        draw_stem(t, length, angle1 / 2)


        draw_roses(t, length * shrink1, min_angle, max_angle, min_shrink, max_shrink, thickness * shrink1)

        t.left(angle1)

        draw_roses(t, length * shrink2, min_angle, max_angle, min_shrink, max_shrink, thickness * shrink2)

        t.right(angle1 / 2)

        t.up()
        t.backward(length)
        t.down()

def wrap_roses(t, length, width):

    wrap_colors = ["#a2798f", "#8caba8", "#dadceb"]

    make_wrap(gaia, length, width + 10, wrap_colors[1], 8)

    t.right(5)
    t.forward(10)
    make_wrap(gaia, length- 7, width, wrap_colors[0], 16)

    t.left(8)
    t.forward(10)
    make_wrap(gaia, length - 5, width, wrap_colors[2], 8)

    t.up()
    t.right(8)
    t.color('#330000')


    t.forward(length / 2)

    p0 = t.pos()

    t.left(90)
    t.forward(width - 7)

    p1 = t.pos()

    t.right(75)
    t.forward(10)

    p2 = t.pos()

    t.goto(p0)
    t.right(5)

    t.right(90)
    t.forward(width - 14.5)

    p3 = t.pos()

    t.left(75)
    t.forward(10)

    p4 = t.pos()

    t.goto(p1)
    t.begin_fill()
    t.goto(p2)
    t.goto(p4)
    t.goto(p3)
    t.end_fill()












#wn.tracer(0,0)

gaia.left(90)

gaia.hideturtle()

draw_roses(gaia, 35, 10, 30, .7, .8, 5)

wrap_roses(gaia, 110, 25)

#wn.update()

wn.exitonclick()