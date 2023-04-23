"""TextNet GameBoard Class.
This file contains the 'TextNet GameBoard' class, which is the class used to
create the playable in-game maps for the game."""

# Imports
from GameObject import GameObject


class GameBoard:
	SYMBOL_KEY: dict = {
		".": "Empty Space",
		"#": "Game Object",
		"*": "Player",
		"!": "Enemy",
		"|": "Vertical Wall",
		"+": "Wall Cross-Section",
		"-": "Horizontal Wall"
	}
	
	def __init__(self, width: int = 15, height: int = 15, difficulty: float = 0.1):
		"""This method is the constructor for the GameBoard class.
		It is called automatically upon the creation of GameObject objects."""
		self.width = width
		self.height = height
		self.difficulty = difficulty
		self.data_table: list = []
		
		for row in range(height):
			temp_column: list = []
			for col in range(width):
				temp_column.append(None)
			self.data_table.append(temp_column)
	
	def __str__(self):
		"""This method defines the return value of objects of the GameBoard
		class.
		An example use-case would be when you use print() function statement, or
		when if you want to assign the value of a variable to this class' return
		value."""
		return_string: str = ""
		for row in self.data_table:
			temp_string: str = ""
			for column in row:
				if type(column) == type(None):
					column = "."
				elif type(column) == type(GameObject("placeholder")):
					column = "#"
				else:
					column = " "
				temp_string += "[" + str(column) + "]"
			return_string += temp_string + "\n"
		return return_string
	
	def start(self):
		"""This method is called once, when the GameBoard object is initialised.
		Objects are usually initialised when the game first starts running."""
		raise NotImplementedError("The start() method for this class has not been implemented yet.")
	
	def update(self):
		"""This method is called once every frame."""
		raise NotImplementedError("The update() method for this class has not been implemented yet.")


test_board: GameBoard = GameBoard(5, 5, 1.0)
print(test_board)
