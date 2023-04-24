"""TextNet GameObject class + child classes.

This file contains the baseclasses for every in-game object.
These are as follows:

 1) 'GameObject' class - The baseclass for all possible in-game object classes
    to inherit from.
 
 2) 'Item' class - The baseclass for in-game Item object classes to inherit from
    and for creating Item objects.
 
 3) 'GameEntity' class; the baseclass for creating Entity objects.
 
 4)

There are also example objects of each class in this file."""

# Imports
# import <module>
# from <module> import <thing>


# Possibly an abstract class in final program.
class GameObject(object):
	# If class is abstract, __init__() not to be implemented because abstract
	# classes can't create objects and so can't have constructors.
	def __init__(self, name: str):
		"""This method is the constructor for GameObject class.
		It is called automatically upon the creation of GameObject objects."""
		self.name: str = name
		self.position: tuple[int, int] = (0, 0)

	def start(self):
		"""This method is called once, when the GameObject object is initialised.
		Objects are usually initialised when the game first starts running."""
		raise NotImplementedError("The start() method for this class has not been implemented yet.")
	
	def update(self):
		"""This method is called once every frame."""
		raise NotImplementedError("The update() method for this class has not been implemented yet.")


# Won't work if the class is abstract
example_gameobject: GameObject = GameObject("Example GameObject")


# Also possibly abstract in final program.
class Item(GameObject):
	def __init__(self, name: str):
		super().__init__(name)
	
	def start(self):
		super().start()
	
	def update(self):
		super().update()


example_item: Item = Item("Example Item")


# Also possibly abstract in final program.
class GameEntity(GameObject):
	def __init__(self, name: str, start_pos: tuple[int, int] = (0, 0)):
		super().__init__(name)
		self.start_pos: tuple[int, int] = start_pos
	
	def start(self):
		super().start()
	
	def update(self):
		super().update()


example_entity: GameEntity = GameEntity("Example GameEntity")
