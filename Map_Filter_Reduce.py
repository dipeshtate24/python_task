def cube(x):
    return x **3

l = [1, 2, 4, 6, 4, 3]

new=list(map(cube, l))
print(new)

new1 = list(map(lambda x:x**3, l))
print(new1)

# Filter
def filter_function(a):
    return a > 2

newl = list(filter(filter_function,l))
print(newl)


# Reduce

from functools import reduce

number = [1, 2, 3, 4, 5]

def add_sum(x, y):
    return x + y

# sum = reduce(lambda x, y: x+y, number)
# print(sum)
sum = reduce(add_sum, number)
print(sum)