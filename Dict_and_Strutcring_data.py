# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}

# for character in message:
#     count.setdefault(character, 0)
#     count[character] += 1

# print(count)

# all_guests = {'Alice': {'apples': 5, 'pretzels': 12},
#               'Bob': {'ham sandwiches': 3, 'apples': 2},
#               'Carol': {'cups': 3, 'apple pies': 1}}

# def total_brought(guests, item):
#     num_brought = 0
#     for k, v in guests.items():
#         num_brought += v.get(item, 0)
#     return num_brought

# print('Number of things being brought:')
# print(' - Apples         ' + str(total_brought(all_guests, 'apples')))
# print(' - Cups           ' + str(total_brought(all_guests, 'cups')))
# print(' - Cakes          ' + str(total_brought(all_guests, 'cakes')))
# print(' - Ham Sandwiches ' + str(total_brought(all_guests, 'ham sandwiches')))
# print(' - Apple Pies     ' + str(total_brought(all_guests, 'apple pies')))

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    print("Inventory")
    
    items_total = 0
    for k, v in inventory.items():
        items_total += v
    print("Total number of items:" + str(items_total))

display_inventory(stuff)


def add_to_inventory(inventory, added_item):

    for i in added_item:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1

    print(inventory)

def display_inventory(inventory):
    print("Inventory")
    
    items_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        items_total += v
    print("Total number of items:" + str(items_total))

inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
add_to_inventory(inv, dragon_loot)
display_inventory(inv)
