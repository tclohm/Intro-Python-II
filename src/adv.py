# Modules
import os
import textwrap
from colored import fg, bg, attr
from room import Room
from player import Player
from item import Item

wrapper = textwrap.TextWrapper()
color = { "bold": "\033[1m", "green": "\033[92m", "purple": "\033[95m", "cyan": "\003[96m", "end": "\033[0m"}

# Declare items
flashlight = Item("🔦", "To light the way or attack enemies")
hat = Item("🧢", "To keep the sun out of your eyes")
note = Item("📝", "Reads: turn back there is nothing here")
skull = Item("💀", "A skeleton skull")
money = Item("💵", "$2 dollars")
toy = Item("🪀", "A lost toy")
coconut = Item("🥥", "A coconut")

# Declare all the rooms

room = {
    'outside':  Room("%s Cave Entrance %s" % (bg('indian_red_1a'), attr('reset')),
                     """\033[1mNorth\033[0m of you, the cave mount beckons"""),

    'foyer':    Room("%s Foyer %s" % (bg('dark_cyan'), attr('reset')), 
    			"""Dim light filters in from the \033[1msouth\033[0m. Dusty passages run \033[1mnorth\033[0m and \033[1meast\033[0m."""),

    'overlook': Room("%s Grand Overlook %s" % (bg('dark_turquoise'), attr('reset')), 
    			"""A steep cliff appears before you, falling into the darkness. Ahead to the \033[1mnorth\033[0m, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("%s Narrow Passage %s" % (bg('dark_red_2'), attr('reset')), 
    			"""The narrow passage bends here from \033[1mwest\033[0m to \033[1mnorth\033[0m. The smell of gold permeates the air."""),

    'treasure': Room("🏆%s Treasure Chamber %s🏆" % (bg('gold_3a'), attr('reset')), 
    			"""You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the \033[1msouth\033[0m."""),
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

room['outside'].add(hat, coconut)
room['foyer'].add(skull, flashlight)
room['narrow'].add(note)
room['treasure'].add(toy, money)

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

# Make a new player object that is currently in the 'outside' room.

print("🤖 ------- Welcome to the one and only adventure game ------- 👾")
def start():
	clear()
	print(wrapper.fill(
		"""💬 Before we get started, you'll be using your keyboard to 
		interact with the game. All of your inputs except for your name 
		should be one letter"""))

	understand = input("❓" + color["purple"] + 
		" Would you like to continue? (Y/n): " + color["end"])

	if understand == "y" or understand == "Y" or understand == "":
		print("💬 Alright! Let's go!")
		name = input("❓" + color["purple"] + 
			" Please enter your name: " + color["end"])

		player_one = Player(name, room["outside"])
		clear()
		while True:
			player_choices = { 
				'n': player_one.current_room.n_to, 
				'e': player_one.current_room.e_to, 
				's': player_one.current_room.s_to, 
				'w': player_one.current_room.w_to 
			}
			move = {
				"n": "north", 
				"e": "east", 
				"s": "south", 
				"w": "west", 
				"q": "quit"}
			wrapper.break_on_hyphens = True
			wrapper.drop_whitespace = True
			print("============================================")
			print(wrapper.fill(f"{player_one.current_room}"))
			print("============================================")
			print(f"\n{player_one}")
			print("\n❓" + " What do you want to do?\n")

			input_list = {key for key in move.items()}
			input_string = str(input_list)

			command = input(f"🎮 \033[1m {input_string[1:-1]} \033[0m: ")

			if command == "q":
				clear()
				print("I hope you had fun!\nQuiting the game...goodbye")
				break
			elif command not in player_choices:
				clear()
				print(f"🙅‍♀️ {command} is not an option. 🤦‍♂️")
				
			elif player_choices[command] == None:
				clear()
				print(f"""\n✋✋✋ Unfortunately, {attr('bold')}{move[command].upper()}{attr('reset')} will lead you to nothing. Pick another way ✋✋✋\n""")
				
			else:
				clear()
				print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
				print(f"You moved \033[1m{move[command]}\033[0m leaving the {player_one.current_room.name}")
				print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
				player_one.current_room = player_choices[command]
				

	elif understand == "n" \
	or understand == "N" \
	or understand == "no" \
	or understand == "NO":
		print(f"\nExiting the game\nAlright! Have a good day!\n")
	else:
		print(f"""`{understand}` isn't one of the options....
			\nExiting the game\nGoodbye\n""")


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
