a = 22 
if (a > 9):
    print('grater')
else:
    print('lesser')

age = int(input("Enter your age:"))
if (age > 18):
    print("Your are eligible")
else:
    print("Your are not eligible")

a = None
if a is None:
    print('Yes')
else:
    print('No')


fruits = ['apple', 'mango']

if 'apple' in fruits:
    print('Yes')
else:
    print('No')

if not 'Banana' in fruits:
    print("banana is not in fruits list.")
else:
    print("present in the fruits list.") 

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
num3 = int(input("Enter number 3:"))
num4 = int(input("Enter number 4:"))


if num1 > num2:
    new_1 = num1
else:
    new_1 = num2

if num3 > num4:
    new_2 =num3
else:
    new_2 = num4
# print(num1, num2)
if new_1 > new_2:
    print(new_1)
else:
    print(new_2)


subject_1 = int(input("Enter subject 1 marks:"))
subject_2 = int(input("Enter subject 2 marks:"))
subject_3 = int(input("Enter subject 3 marks:"))

total = subject_1+subject_2+subject_3
average = total/3
print(average)

if subject_1 <= 33 or subject_2 <=33 or subject_3 <= 33:
    print("One or more subjet you not met criteria of above 33%.")
elif average > 40:
    print('pass')
else:
    print('fail')

first_sentence ='make a lot of money'
second_sentence ='buy now'
third_sentence ='subcribe this'
fourth_sentence ='click this'
message = input("Write your message:")
spam = False

if first_sentence in message:
    spam = True
elif second_sentence in message:
    spam = True
elif third_sentence in message:
    spam = True
elif fourth_sentence in message:
    spam = True

if spam:
    print("This is message is spam.")
else:
    print("This not a spam message.")

person_name = ['Abhishek', 'kumar', 'Kushal', 'Pravin']
name = input("Enter your name:")
if name.lower() in person_name.lower():
    print("This name is already present in the list.")
else:
    print("This name is not present in the list.")


marks = int(input("Enter your marks:"))

if marks >= 90 and marks <= 100:
    print("Excellent")
elif marks >= 80 and marks < 90:
    print("A")
elif marks >=70 and marks < 80:
    print("B")
elif marks >=60 and marks < 70:
    print("C")
elif marks >=50 and marks < 60:
    print("D")
else:
    print("F")
