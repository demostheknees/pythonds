import turtle

def draw_triangle(t, points):


    t.up()

    t.goto(points[0][0], points[0][1])

    t.down()


    t.goto(points[1][0], points[1][1])
    t.goto(points[2][0], points[2][1])
    t.goto(points[0][0], points[0][1])




def get_mid(p1, p2):
    return ((p1[0]+p2[0]) / 2, (p1[1]+p2[1]) / 2)


def draw_mountain(t, points, degree):

    draw_triangle(t, points)

    if degree > 0:
        draw_mountain(t, [points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])], degree - 1)

        draw_mountain(t, [points[1], get_mid(points[0], points[1]), get_mid(points[1], points[2])], degree - 1)

        draw_mountain(t, [points[2], get_mid(points[2], points[1]), get_mid(points[0], points[2])], degree - 1)


def main():

    atuin = turtle.Turtle()
    discworld = turtle.Screen()

    points = [[-200, -50], [0, 10], [150, -0]]

    draw_mountain(atuin, points, 5)

    discworld.exitonclick()



main()