def rec_factorial(number):
    """ 1. Write a recursive function to compute the factorial of a number."""

    if number == 0:
        return 1

    if number == 1:
        return 1
    else:
        return number * rec_factorial(number - 1)


def rec_reverse(alist):
    """ 2. Write a recursive function to reverse a list."""

    if len(alist) == 1:
        return alist

    else:
        return rec_reverse(alist[1:]) + [alist[0]]


def call_tree_maker():
    """ 3. Modify the recursive tree program using one or all of the following ideas:

        - Modify the thickness of the branches so that as the branchLen gets smaller, the line gets thinner.

        - Modify the color of the branches so that as the branchLen gets very short it is colored like a leaf.

        - Modify the angle used in turning the turtle so that at each branch point the angle is selected at random
        in some range. For example choose the angle between 15 and 45 degrees. Play around to see what looks good.

        - Modify the branchLen recursively so that instead of always subtracting the same amount you subtract a
        random amount in some range.
    """
    from chapter_4_recursion import c4_visualizing

    c4_visualizing.main()


def call_mountain_maker():
    """4. Find or invent an algorithm for drawing a fractal mountain. Hint: One approach to this uses triangles again. """
    pass


def rec_fib(to_number):
    """5. Write a recursive function to compute the Fibonacci sequence. How does the performance of the recursive
    function compare to that of an iterative version? """

    if to_number == 0:
        return 0

    elif to_number == 1:
        return 1

    else:
        return rec_fib(to_number - 2) + rec_fib(to_number - 1)


def call_hanoi_with_stacks():
    """6. Implement a solution to the Tower of Hanoi using three stacks to keep track of the disks."""

    from chapter_4_recursion.exercises import hanoi_with_stacks

    hanoi_with_stacks.main()


def call_hilbert_curve():
    """ 7. Using the turtle graphics module, write a recursive program to display a Hilbert curve."""

    from chapter_4_recursion.exercises import hilbert_curve

    hilbert_curve.main()


def call_snowflake():
    """8. Using the turtle graphics module, write a recursive program to display a Koch snowflake."""

    from chapter_4_recursion.exercises import koch

    koch.main()


def call_die_hard_riddle():
    """
    9. Write a program to solve the following problem: You have two jugs: a 4-gallon jug and a 3-gallon jug.
    Neither of the jugs have markings on them. There is a pump that can be used to fill the jugs with water. How
    can you get exactly two gallons of water in the 4-gallon jug?

    10. Generalize the problem above so that the parameters to your solution include the sizes of each jug and the
    final amount of water to be left in the larger jug.
    """

    from chapter_4_recursion.exercises import die_hard

    die_hard.solve(3, 4, 2)

def call_cannibals():
    """
    11. Write a program that solves the following problem: Three missionaries and three exercises come to a river and
    find a boat that holds two people. Everyone must get across the river to continue on the journey. However, if the
    exercises ever outnumber the missionaries on either bank, the missionaries will be eaten. Find a series of
    crossings that will get everyone safely to the other side of the river.
    """

    pass

def call_hanoi_turtle():
    """12. Modify the Tower of Hanoi program using turtle graphics to animate the movement of the disks.
    Hint: You can make multiple turtles and have them shaped like rectangles."""

    from chapter_4_recursion.exercises import hanoi_turtle

    hanoi_turtle.main()

def call_pascal():
    """
    13. Pascal’s triangle is a number triangle with numbers arranged in staggered rows such that

    a_nr = n! / r!(n-r)!

    """
