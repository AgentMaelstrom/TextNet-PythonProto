"""TextNet GameObject Class.
This file contains the 'TextNet GameObject' class, which is the baseclass for
all possible in-game objects' classes to inherit from."""


# Possibly to be abstract class in final program.
class GameObject:
	# If class is abstract, __init__() not to be implemented because abstract
	# classes can't create objects and so can't have constructors.
	def __init__(self, name: str, starting_position: tuple[int] | None = None):
		"""This method is the constructor for GameObject class.
		It is called automatically upon the creation of GameObject objects."""
		self.name: str = name
		if starting_position is not None:
			self.position: tuple[int] = starting_position

	def start(self):
		"""This method is called once, when the GameObject object is initialised.
		Objects are usually initialised when the game first starts running."""
		raise NotImplementedError("The start() method for this class has not been implemented yet.")
	
	def update(self):
		"""This method is called once every frame."""
		raise NotImplementedError("The update() method for this class has not been implemented yet.")
