# Write a class to hold player information, e.g. what room they are in
# currently.

"""
	Player {
		name: String
		current_room: Room { get set }
		inventory: [Item]
	}
"""

class Player:
	def __init__(self, name, current_room, inventory=None):
		self.name = name
		self.__current_room = current_room
		if inventory is None:
			self.inventory = []
		else:
			self.inventory = inventory

	def add(self, item):
		if len(self.inventory) < 2:
			print(f"You've added {item} to your inventory")
			self.inventory.append(item)
			self.__current_room.items.remove(item)
		else:
			print("You're encumbered! You can't carry anymore")
			print(f"Please remove one of your items if you want to carry {item}\n")


	def remove(self, item):
		self.inventory.remove(item)
		self.__current_room.add(item)

	def set_current_room(self, current_room):
		if not current_room:
			raise Exception("Not valid") 
		else: 
			self.__current_room = current_room

	def get_current_room(self):
		return self.__current_room

	current_room = property(get_current_room, set_current_room)

	def __str__(self):
		return "%s inventory: %s" % (self.name + "'s", [item.description for item in self.inventory])
