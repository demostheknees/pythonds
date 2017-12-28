from pack.data_structures import Stack


left = Stack("A")
center = Stack("B")
right = Stack("C")

def move_tower(height, from_pole, to_pole, with_pole):

    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)

        move_disk(from_pole, to_pole, with_pole)

        move_tower(height - 1, with_pole, to_pole, from_pole)


def move_disk(from_pole, to_pole, with_pole):
    move = from_pole.pop()
    to_pole.push(move)
    print("moved disk", move, "from tower", from_pole, "to tower", to_pole)
    print(from_pole.items)
    print(to_pole.items)
    print(with_pole.items)



def main():

    start_height = 3

    for i in range(start_height, 0, -1):
        left.push(i)

    move_tower(start_height, left, center, right)