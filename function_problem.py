def percentage(marks):
    average = (sum(marks)/(len(marks) * 100)) * 100
    return average

p = percentage([75, 98, 88, 78])
print(p)


def greet(name):
    return "Hello, Good Day" + " " + name
print(greet('Manish'))

def mysum(num1, num2):
    return num1+num2

print(mysum(5, 10))


def factorial(n):
    total = 1
    for i in range(1, n+1):
        total *= i
    return total
print(factorial(5))


def recersive_fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recersive_fact(n-1)
    
print(recersive_fact(5))


def maximum(num1, num2, num3):
    if num1 > num2:
        num_new1 = num1
    else:
        num_new1 = num2

    if num_new1 > num3:
        return num_new1
    else:
        return num3

print(maximum(45, 98, 78))



def farh(c):
    return c*(9/5) + 32

print(farh(45))

print("Hello", end="\n")
print("are", end="\n")
print("you!", end="\n")

def fab(n):
    for i in range(5):
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            return fab(n-1) + fab(n-2)

print(fab(5))

def natural_sum(n):
    if n == 1:
        return 1
    else:
        return n + natural_sum(n-1)

print(natural_sum(5)) 

new_list = ["apple", "mango"]
for i in new_list:
    if "apple" == i:
        new_list.remove(i)
    print(new_list) 


def CalculateGmean(a, b):
    mean = (a * b) / (a + b)
    print(round(mean,2))    

def isGrater(a, b):
    if a > b:
        print("First number is grater.")
    else:
        print("Second number is grater and equal.")

CalculateGmean(9, 8)
isGrater(9, 8)
