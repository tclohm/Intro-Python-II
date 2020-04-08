# Modules
from room import Room
from player import Player

color = { "bold": "\033[1m", "green": "\033[92m", "purple": "\033[95m", "cyan": "\003[96m", "end": "\033[0m"}

# Declare all the rooms

room = {
    'outside':  Room("Cave Entrance",
                     "\033[1mNorth\033[0m of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the \033[1msouth\033[0m`. Dusty
passages run \033[1mnorth\033[0m and \033[1meast\033[0m."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the \033[1mnorth\033[0m, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from \033[1mwest\033[0m
to \033[1mnorth\033[0m. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the \033[1msouth\033[0m."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

print("💻 ------- Welcome to the one and only adventure game ------- 🎮")
def start():
	print("💬 Before we get started, you'll be using your keyboard to interact with the game. All of your inputs" + color["bold"] + " except " + color["end"] + "for your" + color["bold"] + " name " + color["end"] + "should be one letter")
	understand = input("❓" + color["purple"] + " Would you like to continue? (Y/n): " + color["end"])

	if understand == "y" or understand == "Y" or understand == "":
		print("Alright! Let's go!")
		name = input("❓" + color["purple"] + " Please enter your name: " + color["end"])
		player_one = Player(name, room["outside"])
		player_choices = { 'n': player_one.current_room.n_to, 'e': player_one.current_room.e_to, 's': player_one.current_room.s_to, 'w': player_one.current_room.w_to }

		while True:
			inputs = {"n": "north", "e": "east", "s": "south", "w": "west", "q": "quit"}

			print(f"\n{player_one.current_room}")
			print("❓" + " Which way will you go?\n")
			print(inputs)
			command = input(f"\033[1m {[((key),value) for key, value in inputs.items()]} \033[0m")

			if command == "q":
				print("quiting the game...goodbye")
				break
			elif command not in player_choices:
				print(f"🙅‍♀️ {command} is not an option. 🤦‍♂️")
				pass
			elif player_choices[command] == None:
				print("\n✋Unfortunately that will lead your to an nothing. Pick another way")
				pass
			else:
				player_one.current_room = player_choices[command]
				inputs = inputs_original
				pass

	elif understand == "n" or understand == "N" or understand == "no" or understand == "NO":
		print(f"\nExiting the game\nAlright! Have a good day!\n")
	else:
		print(f"`{understand}` isn't one of the options....\nExiting the game\nGoodbye\n")


start()
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
