def person(name):
    return f"hello, {name}"

print(person('suresh'))

# print("hello world")

a = 5 
b = 6

print(a+b)

# print("hello world")

a = 5 
b = 6
print(a+b)

n = 5 
for i in range(1, 11):
    print(f"{n} x {i} = ", n*i)

# P (Principle) = initial amount borrowed
# r (Rate) = Annual Rate 
# t (Time) =  Time period in years

def simple_interest(P, r, t):
    r = r/100
    SI = P*r*t
    return SI

a = simple_interest(10000, 5, 3)
print(a)


import random
list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
a = random.choice(list_number)
print(a)
for i in range(0, len(list_number)):
    n = int(input("Enter number:"))
    if n == a:
        
        print('guess number is correct')
        print(count)
    else:
        print('guess number is not correct. please try again.')
        count += 1
