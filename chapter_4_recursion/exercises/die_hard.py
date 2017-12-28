import math


class Jug():

    def __init__(self, size):
        self.size = size
        self.filled = 0
        self.cap = size




    def fill(self):
        self.filled += self.size
        self.cap -= self.size


    def empty(self):
        self.filled -= self.filled
        self.cap += self.size

    def transfer(self, jug):
        if self.filled >= jug.cap:
            jug.filled += jug.cap
            self.filled -= jug.cap
            self.cap += jug.cap
            jug.cap = 0

        else:
            jug.filled += self.filled
            jug.cap -= self.filled
            self.cap += self.filled
            self.filled = 0

    def is_empty(self):
        if self.filled == 0:
            return True

    def is_full(self):
        if self.filled == self.size:
            return True

def check(jug_a, jug_b, step):
    print('----', step, '----' "\n")
    print(jug_a.size, "Gallon Jug:", jug_a.filled, "|", jug_b.size, "Gallon Jug:", jug_b.filled, "\n")
    print(jug_a.size, "Gallon Jug can take", jug_a.cap, "\n")
    print(jug_b.size, "Gallon Jug can take", jug_b.cap, "\n")
    print('--------------', "\n")








def solve(m, n, d):

    if d % math.gcd(m, n):
        print("Not solvable")
    else:

        m = Jug(m)
        n = Jug(n)
        steps = 0

        while n.filled != d and m.filled != d:

            n.transfer(m)
            check(m, n, steps)

            if n.is_empty():
                n.fill()


            if m.is_full():
                m.empty()

            steps += 1


        print("Found", [m.filled, n.filled], "in", steps, "Steps")

solve(3, 4, 2)



