# Makena Bustos

# The dictionary links a room to other rooms and items
rooms = {
    'Foyer': {'North': 'Kitchen', 'East': 'Armory', 'South': 'Storage Room', 'West': 'Office'},
    'Kitchen': {'East': 'Alchemy Room', 'South': 'Foyer', 'item': 'Potion'},
    'Alchemy Room': {'West': 'Kitchen', 'item': 'Gem'},
    'Craft Room': {'South': 'Armory', 'item': 'Ammo'},
    'Armory': {'North': 'Craft Room', 'West': 'Foyer', 'item': 'Gun'},
    'Bedroom': {'West': 'Storage Room', 'item': 'Picture'},
    'Storage Room': {'North': 'Foyer', 'East': 'Bedroom', 'item': 'Rabbit'},
    'Office': {'East': 'Foyer', 'item': 'Enforcer'}  # Villain
}


# Player Instructions and Intro
def show_instructions():
    return ("Spy Text Game "
            "\nCollect 6 items to win the game, or be caught by the Enforcer "
            "\nMove commands: go South, go North, go East, go West "
            "\nAdd to Inventory: get 'item name'"
            "\nExit: Exit Game"
            "\n")


def move_rooms(pos, direct):
    pos = rooms[pos][direct]
    return pos


def get_item(inventory, items):
    inventory.insert(0, items)
    return print("You got the item!")


# Displays the player's current status
def show_status(pos, items, inventory):
    print('-' * 20)
    print('You are in the {}'.format(pos))
    print('Inventory: {}'.format(inventory))
    if pos != 'Foyer' and items not in inventory:
        print("You see a {}".format(items))
    print("-" * 20)


# Starting settings for player
user_pos = 'Foyer'  # Starting Room
inv = []  # Player must start with no items in inventory
user_input = ''
current_item = ''

print(show_instructions())

while user_input != 'Exit Game':
    show_status(user_pos, current_item, inv)
    possible_moves = rooms[user_pos].keys()
    print('Possible Moves:')
    for key in possible_moves:  # Loop that prints all possible moves minus 'item'
        if key == 'item':
            continue
        print(key, end=' ')
    user_input = input('\nEnter move: ')
    split_input = user_input.split()
    second_act = split_input.pop()
    second_act = second_act.capitalize()
    first_act = split_input.pop()

    if first_act == 'go':
        if second_act in possible_moves:
            user_pos = move_rooms(user_pos, second_act)
            try:
                current_item = rooms[user_pos]['item']
            except KeyError:
                continue
            if (user_pos == 'Foyer') or (current_item in inv):
                continue

    elif first_act == 'get':
        if second_act == current_item:
            get_item(inv, current_item)
    else:
        user_input = input("INVALID MOVE, try again: ")

# Endings if they enter the Office with or without 6 items
    if (user_pos == 'Office') and len(inv) == 6:
        print("YOU WON! CONGRATULATIONS")
        exit()
    elif (user_pos == 'Office') and (len(inv) < 6):
        print('YOU LOST! GAME OVER!!')
        exit()
    else:
        continue
print('Goodbye!')
exit()
