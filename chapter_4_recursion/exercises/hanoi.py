def move_tower(height, from_pole, to_pole, with_pole):
    print("move_tower called,", "height is", height, "\n")

    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        print("at pole", from_pole, "-", "disk", height, "\n")

        move_disk(from_pole, to_pole, height)

        move_tower(height - 1, with_pole, to_pole, from_pole)


def move_disk(fp,tp, disk):
    print("moving disk", disk, "from pole",fp,"to pole",tp, "\n")


move_tower(3, "A", "B", "C")