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


def min_max(lst):
    new_list = []
    if len(lst) > 1:
        new_list.append(min(lst))
        new_list.append( max(lst))
        return new_list
    
    else:
        new_list.append(min(lst))
        new_list.append(1)
        return new_list

print(min_max([1]))

def min_max(lst):
  return [min(lst), max(lst)]


def persistence(n):
    count = 0

    while n >= 10:
        product = 1
        
        for digit in str(n):
            product *= int(digit)
        
        n = product
        count += 1
    return print(count)
persistence(39)