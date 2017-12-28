import turtle

hilbert = turtle.Turtle()
hilbert.speed("slowest")
hilbert.pensize("3")

space = turtle.Screen()







def curve(turtle, size, angle, order):

    colors = ["green", "black"]



    if order == 0:
        pass

    else:
        space.onclick(turtle.color(colors[0]))
        space.listen()

        space.onclick(turtle.right(angle))
        #print("starting curve -------------")
        #print("turning", angle, "degrees", "\n")

        #curve(turtle, size, -angle, order - 1)

        #turtle.forward(size)
        #print("going forward", size, "\n")

        #turtle.left(angle)
        #print("turning", angle, "degrees", "\n")

        #curve(turtle, size, angle, order - 1)

        #turtle.forward(size)
        #print("going forward", size, "\n")

        #curve(turtle, size, angle, order - 1)

        #turtle.left(angle)
        #print("turning", angle, "degrees", "\n")

        #turtle.forward(size)
        #print("going forward", size, "\n")

        #curve(turtle, size, -angle, order - 1)


        #turtle.right(angle)
        #print("turning", angle, "degrees")
        #print("ending curve ---------------", "\n")

        space.onclick(turtle.color(colors[1]))

space.listen()

curve(hilbert, 10, 90, 3)

space.mainloop()