name = ''
while name != 'your name':
    print('please type your name.')
    name = input('>')
print("Thank you")


while True:
    print('please type your name.')
    name = input('>')
    if name == 'your name':
        break
print("Thank you")

while True:
    print("who are you?")
    name = input('> ')
    if name != 'Joe':
        continue
    print('Hello, Joe. What is your password? (It is fish)')
    password = input('> ')
    if password == 'Swordfish':
        break
print('Access Granted.')

name = ''
while not name:
    print('Enter your name')
    name = input('> ')
print('How many guest will you have?')
no_of_guest = int(input('> '))
if no_of_guest:
    print('Be sure to have enough room for all your guests.')
print('Done.')

import sys

while True:
    print('Type exit to exit.')
    response = input('> ')
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + ' .')


import random, sys

print('ROCK, PAPER, SCISSORs')

# The number keep track of number of wins, losses, and ties
wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' %(wins, losses, ties))

    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input('> ')
        if player_move == 'q':
            sys.exist()
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break
        print('Type of one r, p, s, or q.')

    # Display what the player choose
    if player_move == 'r':
        print('rock versus...')
    elif player_move == 'p':
        print('paper versus...')
    elif player_move == 's':
        print('scissor versus...')

    # Display what computer choose
    computer_move = random.randint(1,3)

    if computer_move == '1':
        computer_move = 'r'
        print('rock')
    elif computer_move == '2':
        computer_move = 'p'
        print('paper')
    elif computer_move == '3':
        computer_move = 's'
        print('scissor')

    if player_move == computer_move:
        print("it is a tie.")
        ties += 1
    elif player_move == 'r' and computer_move == 's':
        print('You win!')
        wins += 1
    elif player_move == 's' and computer_move == 'p':
        print('You win!')
        wins += 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win!')
        wins += 1
    elif player_move == 's' and computer_move == 'r':
        print('You lose!')
        losses += 1
    elif player_move == 'p' and computer_move == 's':
        print('You lose!')
        losses += 1
    elif player_move == 'r' and computer_move == 'p':
        print('You lose!')
        losses += 1 
