def cube(x):
    return x **3

l = [1, 2, 3, 4, 5]

new=list(map(cube, l))
print(new)