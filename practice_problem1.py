
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