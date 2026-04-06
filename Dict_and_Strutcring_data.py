# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}

# for character in message:
#     count.setdefault(character, 0)
#     count[character] += 1

# print(count)

all_guests = {'Alice': {'apples': 5, 'pretzels': 12},
              'Bob': {'ham sandwiches': 3, 'apples': 2},
              'Carol': {'cups': 3, 'apple pies': 1}}

def total_brought(guests, item):
    num_brought = 0
    for k, v in guests.items():
        num_brought += v.get(item, 0)
    return num_brought

print('Number of things being brought:')
print(' - Apples         ' + str(total_brought(all_guests, 'apples')))
print(' - Cups           ' + str(total_brought(all_guests, 'cups')))
print(' - Cakes          ' + str(total_brought(all_guests, 'cakes')))
print(' - Ham Sandwiches ' + str(total_brought(all_guests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(total_brought(all_guests, 'apple pies')))
