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

	count = 0

	# MARK: -- helper function for setter and getters
	def setRoom(self, direction, room):
		if not room:
			raise Exception("Invalid Room")
		self.direction = room


	def __init__(self, name, description, n_to=None, e_to=None, s_to=None, w_to=None):
		self.name = name
		self.description = description
		self.__n_to = n_to
		self.__e_to = e_to
		self.__s_to = s_to
		self.__w_to = w_to
		Room.count += 1

	# MARK: -- north
	def set_n_to(self, room):
		if not room:
			raise Exception("Invalid Room")
		self.__n_to = room

	def get_n_to(self):
		return self.__n_to

	# MARK: -- east
	def set_e_to(self, room):
		if not room:
			raise Exception("Invalid Room")
		self.__e_to = room

	def get_e_to(self):
		return self.__e_to

	# MARK: -- south
	def set_s_to(self, room):
		if not room:
			raise Exception("Invalid Room")
		self.__s_to = room

	def get_s_to(self):
		return self.__s_to

	# MARK: -- west
	def set_w_to(self, room):
		if not room:
			raise Exception("Invalid Room")
		self.__w_to = room

	def get_w_to(self):
		return self.__w_to

	n_to = property(get_n_to, set_n_to)
	e_to = property(get_e_to, set_e_to)
	s_to = property(get_s_to, set_s_to)
	w_to = property(get_w_to, set_w_to)

	def __str__(self):
		return f"\t{self.name}\n=======================================\n{self.description}\n"

	def __repr__(self):
		return f"Room: {self.name} \nDescription: {self.description}"

	@classmethod
	def getCount(cls):
		return f"There are {cls.count} rooms"
