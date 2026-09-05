for i in [0, 1, 2, 3]:
    print(i)

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index '+ str(i) + ' in supplies '+ supplies[i])

my_pets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter your pet name.')
pet_name = input('> ')
if pet_name is not my_pets:
    print('I dont have a pet named '+ pet_name)
else:
    print(pet_name + ' is my pet.')

n = [1, 2, 3, 4]
b = n.pop(3)
a = n.pop(0)
n.append(a)
n.insert(0, b)
print(n)

n[0], n[-1] = n[-1], n[0]
print(n)

spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
print(spam)

spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)


import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print('Ask a yes or no question:')
input('> ')
print(messages[random.randint(0, len(messages)-1)])

x = 'hello'
word = list(x)
print(word)
dict_word = {}
for i in word:
    dict_word[i]  = word.count(i)

print(dict_word)

print([int(int('3'*2)//11)])

