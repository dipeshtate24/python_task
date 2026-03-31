# name = ''
# while name != 'your name':
#     print('please type your name.')
#     name = input('>')
# print("Thank you")


# while True:
#     print('please type your name.')
#     name = input('>')
#     if name == 'your name':
#         break
# print("Thank you")

# while True:
#     print("who are you?")
#     name = input('> ')
#     if name != 'Joe':
#         continue
#     print('Hello, Joe. What is your password? (It is fish)')
#     password = input('> ')
#     if password == 'Swordfish':
#         break
# print('Access Granted.')

# name = ''
# while not name:
#     print('Enter your name')
#     name = input('> ')
# print('How many guest will you have?')
# no_of_guest = int(input('> '))
# if no_of_guest:
#     print('Be sure to have enough room for all your guests.')
# print('Done.')

import sys

while True:
    print('Type exit to exit.')
    response = input('> ')
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + ' .')