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

	def pickup(self, item):
		if len(self.inventory) <= 2:
			self.current_room.items.remove(item)
			self.inventory.append(item)
		else:
			raise Exception(f"You are carrying too many things. Please drop an item from your inventory to pick up {item}")


	def drop(self, item):
		self.inventory.remove(item)
		self.current_room.add(item)

	def set_current_room(self, current_room):
		if not current_room:
			raise Exception("Not valid") 
		else: 
			self.__current_room = current_room

	def get_current_room(self):
		return self.__current_room

	current_room = property(get_current_room, set_current_room)

	def __str__(self):
		return "%s inventory: %s" % (self.name + "'s" if self.name[-1] != "s" else self.name + "'", self.inventory)
