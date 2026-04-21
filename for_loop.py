colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)

for i in range(4, 10):
    print(i)


for i in range(1, 12, 3):
    print(i)

for x in range(5):
    print("iteration no {} in for loop".format(x+1))
else:
    print("else block in loop")
print("Out of loop")
