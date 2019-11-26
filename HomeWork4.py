
def max_length(*lists):
    return max(list(map(lambda l: len(l), *lists)))

def my_zip(*lists):
    ml = max_length(lists)
    for l in lists:
        r = ml - len(l)
        if r != 0:
            for i in range(r):
                l.append(None)
    return tuple(map(lambda *x: x, *lists))

l = ['mptu', 2, 3, 9]
ll = ['yare', 7, 6, 5, 4]
lll = ['fff', 10, 20, '30tri', 40, 50]
def task2():
    print(str(my_zip(l, ll, lll)))

task2()