# Write a class to hold player information, e.g. what room they are in
# currently.

"""
	Player {
		name: String
		current_room: Room { get set }
	}
"""

class Player:
	def __init__(self, name, current_room):
		self.name = name
		self.current_room = current_room

	def set_current_room(self, current_room):
		self.current_room = current_room

	def get_current_room(self):
		return self.current_room

	current_room = property(set_current_room, get_current_room)

