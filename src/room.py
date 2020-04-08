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
		self._n_to = n_to
		self._e_to = e_to
		self._s_to = s_to
		self._w_to = w_to
		Room.count += 1

	# MARK: -- north
	def _set_n_to(self, room):
		if not room:
			raise Exception("Invalid Room")
		self._n_to = room

	def _get_n_to(self):
		return self._n_to

	# MARK: -- east
	def _set_e_to(self, room):
		if not room:
			raise Exception("Invalid Room")
		self._e_to = room

	def _get_e_to(self):
		return self._e_to

	# MARK: -- south
	def _set_s_to(self, room):
		if not room:
			raise Exception("Invalid Room")
		self._s_to = room

	def _get_s_to(self):
		return self._s_to

	# MARK: -- west
	def _set_w_to(self, room):
		if not room:
			raise Exception("Invalid Room")
		self._w_to = room

	def _get_w_to(self):
		return self._w_to

	n_to = property(_get_n_to, _set_n_to)
	e_to = property(_get_e_to, _set_e_to)
	s_to = property(_get_s_to, _set_s_to)
	w_to = property(_get_w_to, _set_w_to)

	def __str__(self):
		return f"Room: {self.name} \nDescription: {self.description}.\n"

	def __repr__(self):
		return f"Room: {self.name} \nDescription: {self.description}"

	@classmethod
	def getCount(cls):
		return f"There are {cls.count} rooms"
