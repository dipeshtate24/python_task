# x = 4 # global variable
# print(x)

# def hello():
#     x = 5 # local variable

#     print(f"local value of x is {x}")
#     print("Hey friend")

# print(f"global value is x is {x}")
# hello()
# print(f"global value is x is {x}")


x = 4 # global variable
print(x)

def hello():
    global x
    x = 5 # local variable

    print(f"local value of x is {x}")
    print("Hey friend")

print(f"global value is x is {x}")
hello()
print(f"global value is x is {x}")