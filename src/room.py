# Implement a class to hold room information. This should have name and
# description attributes.

"""
	Room {
		name: String
		description: Int
		
		n_to { get set }
		e_to { get set }
		s_to { get set }
		w_to { get set }
	}
"""
class Room:

	room_count = 0

	def __init__(self, name, description):
		self.name = name
		self.description
		Room.count += 1

	# MARK: -- helper function for setter and getters
	def setRoom(self, direction, room):
		if not room and type(room) != type(Room):
			raise Exception("Invalid Room")
		self.direction = self.room

	# MARK: -- north
	def set_n_to(self, n_to, room):
		setRoom(n_to, room)

	def get_n_to(self):
		return self.n_to

	# MARK: -- east
	def set_e_to(self, room):
		setRoom(e_to, room)

	def get_e_to(self):
		return self.e_to

	# MARK: -- south
	def set_s_to(self, room):
		setRoom(s_to, room)

	def get_s_to(self):
		return self.s_to

	# MARK: -- west
	def set_w_to(self, room):
		setRoom(s_to, room)

	def get_w_to(self):
		return self.w_to

	n_to = property(get_n_to, set_n_to)
	e_to = property(get_e_to, set_e_to)
	s_to = property(get_s_to, set_s_to)
	w_to = property(get_w_to, set_w_to)

	def __str__(self):
		return f"Room: {self.name} \nDescription: {self.description}.\n"

	def __repr__(self):
		return f"Room: {self.name} \nDescription: {self.description}"

	@classmethod
	def getCount(cls):
		return f"There are {cls.room_count} rooms"
