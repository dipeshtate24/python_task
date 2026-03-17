with open('another.txt', 'r') as f:
    a = f.read()

with open('another.txt', 'w') as f:
    a = f.write('I like mangoes.')

print(a)


with open('another.txt', 'r') as f:
    a = f.readline(5)

with open('another.txt', 'a') as f:
    a = f.write('i am appending')

print(a)
