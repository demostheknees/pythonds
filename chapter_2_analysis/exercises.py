import timeit


# Exercise One

def test1_1():
    alist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for x in alist:
        return alist.index(x)


def test1_2():
    blist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 100, 77, 88, 99]
    for x in blist:
        return blist.index(x)


print("Exercise One:", '\n')

e1t1 = timeit.Timer("test1_1()", "from __main__ import test1_1")
print("List.index() a list", e1t1.timeit(number=1000), "milliseconds")

e1t2 = timeit.Timer("test1_2()", "from __main__ import test1_2")
print("List.index() b list", e1t2.timeit(number=1000), "milliseconds", '\n')


# Exercise Two

def test2_1():
    adict = {}
    for i in range(3000):
        adict[i] = i
    return adict


def test2_2():
    bdict = {}
    for i in range(2000):
        bdict.get(i)


print("Exercise Two:", '\n')

e2t1 = timeit.Timer("test2_1()", "from __main__ import test2_1")
print("List.index() a list", e2t1.timeit(number=1000), "milliseconds")

e2t2 = timeit.Timer("test2_2()", "from __main__ import test2_2")
print("List.index() b list", e2t2.timeit(number=1000), "milliseconds")