import turtle
import random


def drawSpiral(turtle, lineLen):
    if lineLen > 0:
        turtle.forward(lineLen)
        turtle.right(90)
        drawSpiral(turtle, lineLen - 5)


def drawBranch(length, turtle, angle):
    """Draws a single branch segment. Made separate to improve readability of recursive functions"""
    turtle.forward(length)
    turtle.right(angle)


def drawTreeSimple(turtle, branchLength, branchAngle, decreaseBy):
    """Draws the basic fractal tree with the given parameters, good for visualizing the complexity of the tree"""
    newLength = branchLength - decreaseBy

    if branchLength < 1:
        pass  # Base Case

    else:
        drawBranch(branchLength, turtle, branchAngle)
        drawTreeSimple(turtle, newLength, branchAngle, decreaseBy)
        turtle.left(branchAngle * 2)
        drawTreeSimple(turtle, newLength, branchAngle, decreaseBy)
        turtle.right(branchAngle)
        turtle.backward(branchLength)


def drawTreePretty(turtle, branchLength, minLength, thickness, minThickness, minAngle, maxAngle, minShrink, maxShrink):
    """Randomizes the parameters given in order to draw a more realistic tree. Most of the math and structure is lifted from a lecture PDF I found."""

    leafAngle = random.uniform(1, 180)
    fullness = random.randint(1,3)

    leafColors = ['#008000','#007300']
    branchColors = ['#733900','#804000']

    if thickness > minThickness + 3:
        turtle.color(random.choice(branchColors))
    else:
        turtle.color(random.choice(leafColors))
        for i in range(fullness):
            turtle.tilt(leafAngle)
            turtle.stamp()
        turtle.color(random.choice(branchColors))



    if (branchLength < minLength) or (thickness < minThickness):
        pass  # Base Case

    else:
        angleOne = random.uniform(minAngle, maxAngle)  # Randomizing the angle that the branches can be
        angleTwo = random.uniform(minAngle, maxAngle)

        shrinkOne = random.uniform(minShrink, maxShrink)  # Randomizing the amount that branch thickness and length are reduced by each recursive call.
        shrinkTwo = random.uniform(minShrink, maxShrink)

        turtle.pensize(thickness)

        # Core of the function.

        drawBranch(branchLength, turtle, angleOne)


        drawTreePretty(turtle, branchLength * shrinkOne, minLength, thickness * shrinkOne, minThickness, minAngle,
                       maxAngle, minShrink, maxShrink)

        turtle.left(angleOne + angleTwo)

        drawTreePretty(turtle, branchLength * shrinkTwo, minLength, thickness * shrinkTwo, minThickness, minAngle,
                       maxAngle, minShrink, maxShrink)


        turtle.right(angleTwo)
        turtle.pensize(thickness)




        turtle.up()
        turtle.backward(branchLength)
        turtle.down()


def main():

    branchLength = 100  # Setting the variables here for easier adjustment.
    minLength = 10
    minAngle = 5
    maxAngle = 50
    thickness = 10
    minThickness = 1
    minShrink = .7
    maxShrink = .9

    gaia = turtle.Turtle() # Creating the turtle
    gaia.speed(0)




    window = turtle.Screen()  # Creating the screen
    x, y = 3000, 3000
    window.setworldcoordinates(-x, -y, x, y)

    #window.tracer(0,0)  # Comment out to watch the drawing happen. VERY SLOW.
    #gaia.hideturtle()
    gaia.left(90)



    drawTreePretty(gaia, branchLength, minLength, thickness, minThickness, minAngle, maxAngle, minShrink, maxShrink)





    #indow.update() # Updates the screen with the finished drawings.

    window.exitonclick()


main()