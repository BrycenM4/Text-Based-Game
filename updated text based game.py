# Brycen McEuen    IT-140

# introduce player to the game and its commands
print("Welcome to The Killer's Lair Escape Game!")
print('Collect six items to win the game, or be found by the serial killer.')
print('Move Commands: go north, go south, go east, go west, exit')
print("Add to inventory: get 'item name'")

# create a dictionary for the rooms in the game
rooms = {
    'Garage': {'East': 'Kitchen'},
    'Kitchen': {'North': 'Gun Range', 'South': 'Bedroom', 'East': 'Armory', 'West': 'Garage', 'Item': 'Knife'},
    'Gun Range': {'South': 'Kitchen', 'East': 'Weapons Vault', 'Item': 'Pistol'},
    'Weapons Vault': {'West': 'Gun Range', 'Item': 'Sword'},
    'Bedroom': {'North': 'Kitchen', 'East': 'Bathroom', 'Item': 'Baseball Bat'},
    'Bathroom': {'West': 'Bedroom', 'Item': 'First Aid Kit'},
    'Armory': {'West': 'Kitchen', 'North': 'Torture Chamber', 'Item': 'Bulletproof Vest'},
    'Torture Chamber': {'South': 'Armory', 'Boss': 'Serial Killer'}

}
# tell user what room they start out in
current_room = 'Garage'
# create list for players inventory
inventory = []

# create loop for the players movement and inventory
while True:
    print('-' * 25)
    # tell the user what room they are currently in
    print(f'You are in the {current_room}\nInventory: {inventory}')
    # configure when items are nearby
    if 'Item' in rooms[current_room].keys():
        nearby_item = rooms[current_room]['Item']
        print(f'You see a {nearby_item}')
    # Boss Encounter
    if 'Boss' in rooms[current_room].keys():
        # Loss condition
        if len(inventory) < 6:
            print("-" * 25)
            print("Game Over...")
            print(f"You lost a fight with the {rooms[current_room]['Boss']}.")
            print("Thanks for playing! Hope you enjoyed it.")
            break
        # Win Condition
        else:
            print(f"Congratulations! You had the necessary tools to beat the {rooms[current_room]['Boss']}!")
            break

    print("-" * 25)
    # get input from user
    command = input('Enter a command: \n').strip()

    item = "Item"

    next_move = command.split(' ')

    action = next_move[0].title()

    direction = "null"

    if len(next_move) > 1:
        item = next_move[1:]
        direction = next_move[1].title()

        item = " ".join(item).title()

    # Moving between rooms
    if action == "Go":

        try:
            current_room = rooms[current_room][direction]
            print(f"You traveled {direction}")

        except:
            print("You can't go that way.")

    # Picking up items
    elif action == "Get":
        try:
            if item == rooms[current_room]["Item"]:

                if item not in inventory:

                    inventory.append(rooms[current_room]["Item"])
                    print(f"{item} retrieved!")
                    del rooms[current_room]["Item"]

                else:
                    print(f"You already have a {item}.")

            else:
                print(f"Invalid command.")
        except:
            print(f"Invalid command.")

    # creating a way for the user to exit the game
    elif action == "Exit":
        print("Thanks for playing! See you next time.")
        break
    # if a command is invalid
    else:
        print("Invalid command")