import random 

for i in range(10):
    if random.randint(0,1) == 0:
        print('H', end =' ')
    else:
        print('T', end =' ')

print('cats', 'dogs', 'mice')

print('cats', 'dogs', 'mice', sep=',')

def spam(divide_by):
    try:
        return 42/divide_by
    
    except ZeroDivisionError:
        print('Error: Invalid argument')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

def spam(divide_by):
    return 42/divide_by

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))

    
except ZeroDivisionError:
    print('Error: Invalid argument')

import random 
# random_number = random.randint(1, 6)

def get_random_dice_roll():
    random_number = random.randint(1, 6)
    return random_number

print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())


print("Enter integer Number")
number = input('> ')
try:
    print(int(number))

except ValueError:
    print('Number must be integer.')
