

def n_choose_k(n, k):
        return int(n * ((n + 1 - k) / k))

def pascal_line(row):

    line = []
    line.append(1)

    for i in range(row):
        n = row - i
        k = i + 1
        line.append(int(line[i] * (n / k)))

    return line


def pascal_triangle(rows):

    triangle = []

    for row in range(rows):
        triangle.append(pascal_line(row))

    return triangle








