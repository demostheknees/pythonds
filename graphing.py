from chapter_4_recursion.exercises import pascal
import timeit
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

rows =[]
seconds = []


for value in range(20, 200, 20):

    rows.append(value)
    seconds.append(timeit.timeit("pascal.pascal_triangle(value)", setup= "from __main__ import pascal, value", number= 100))

for i in range(len(rows)):
    print(rows[i], seconds[i])



ax.plot(rows, seconds)
plt.show()






