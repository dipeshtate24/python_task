# i = 0
# while i < 10:
#     print("Yes")
#     i += 1
# print("Done")

# fruits = ['Banana', 'Watermelon', 'Grapes', 'Mangoes']
# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1
    
# for i in fruits:
#     print(i)


# for i in range(8):
#     print(i)

# number = int(input("Enter your number:"))
# for i in range(1, 10):
#     print(f"{number} x {i} =", number * i )

# l1 = ["Harry", "Soham", "Sachin", "Rohit"]
# for i in l1:
#     print(f'Hello, {i}')

# number = int(input("Enter your number:"))
# n = 1
# while n < 11:
#     print(f"{number} * {n} =", number * n)
#     n += 1

# number = int(input("Enter your number:"))
# prime = True
# for i in range(2, number):
#     if number % i == 0:
#         prime = False  
#         break
# if prime:
#     print("Given number is prime")
# else:
#     print("Given number is not prime")
       

# n = 5
# total = 0
# start = 1
# while start < n:
#     total += start
#     start += 1
# print(total)

num = int(input("Enter number:"))
fact = 1
for i in range(1,num+1):
    fact *= i
print(fact)
    
