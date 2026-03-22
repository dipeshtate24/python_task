# f = open('sample.txt', 'r')
# data = f.read()
# print(data)

# f = open('sample.txt', 'w')
# p = f.write("let's eat togther.")
# print(p)
# f.close()

# f = open('sample.txt', 'r')
# p = f.readline(5)
# print(p)
# f.close()

# f = open('sample.txt')
# t = f.readlines()
# print(t)

# t = f.readlines()
# print(t)

# f.close()

# f = open('another.txt', 'w')
# f.write("let's play togther.")
# f.close()

f = open('another.txt', 'a')
f.write("I am appending.")
f.close()