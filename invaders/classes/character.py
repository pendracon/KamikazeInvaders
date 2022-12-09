"""
Package of objects representing non-player and player controllable characters
in the game.
"""

from classes.movable_object import MovableObject


class EnemyCharacter(MovableObject):
	"""
	Represents a non-player controllable enemy character in the game.
	"""

	def __init__(self, data):
		"""
		Initializes the enemy character object by loading its image file
		from the given file system path and setting its starting x and y pixel
		positions on screen, the pixel width and height of its on screen image
		("sprite"), its movement rate in pixels, and its score value.

		The parameter 'data' is a map with the required values bound to the
		following keys:
			* 'image'   - the image file path to load from disk.
			* 'xpos'    - the image's x-coordinate on screen
			* 'ypos'    - the image's y-coordinate on screen
			* 'iwidth'  - the image width in pixels
			* 'iheight' - the image height in pixels
			* 'speed'   - the character's movement rate in pixels
			* 'points'  - the enemy's point score value
		"""
		super().__init__(data)
		self.points = data['points']
	# End: def EnemyCharacter.__init__

	def move_x(self, bidirectional=True, min_pos=0, max_pos=0):
		"""
		Moves the character along its horizontal plane in its current
		direction. If the character is bidirectional and is at or beyond its
		minimum or maximum position boundary then its direction is changed
		toward the opposite boundary. Otherwise, the character stops moving
		once it reaches its targeted boundary or is in dying state.
		"""
		super().move_x(bidirectional, min_pos, max_pos)
#		if self.direction_switched:
#			self.move_y(bidirectional, self.min_ypos, self.max_ypos)
	# End: def EnemyCharacter.move_x
# End: class EnemyCharacter


class PlayerCharacter(MovableObject):
	"""
	Represents a player controllable character in the game.
	"""

	def __init__(self, data):
		"""
		Initializes the playable character object by loading its image file
		from the given file system path and setting its starting x and y pixel
		positions on screen, the pixel width and height of its on screen image
		("sprite"), and its movement rate in pixels.

		The parameter 'data' is a map with the required values bound to the
		following keys:
			* 'image'   - the image file path to load from disk.
			* 'xpos'    - the image's x-coordinate on screen
			* 'ypos'    - the image's y-coordinate on screen
			* 'iwidth'  - the image width in pixels
			* 'iheight' - the image height in pixels
			* 'speed'   - the character's movement rate in pixels
		"""
		super().__init__(data)
		self.x_direction = 0
		self.y_direction = 0
	# End: def PlayerCharacter.__init__

	def switch_direction(self):
		"""
		Changes the character's movement direction to the opposite of its
		current direction.
		"""
		if self.x_direction != 0:
			self.x_direction *= -1
		if self.y_direction != 0:
			self.y_direction *= -1
	# End: def Character.switch_direction

	def set_x_direction(self, direction):
		"""
		Updates the character's movement direction along its horizontal plane. A
		positive value (>= 1) sets the character's direction to the right. A
		negative value (<= -1) sets the character's direction to the left.
		"""
		self.x_direction = direction
	# End: def PlayerCharacter.set_x_direction

	def set_y_direction(self, direction):
		"""
		Updates the character's movement direction along its vertical plane. A
		positive value (>= 1) sets the character's direction downward. A
		negative value (<= -1) sets the character's direction upward.
		"""
		self.y_direction = direction
	# End: def PlayerCharacter.set_y_direction

	def move_x(self, min_pos, max_pos):
		"""
		Moves the character along its horizontal plane in its current direction.
		If the character is at or past its minimum (left) or maximum (right)
		positional boundary then further movement in the boundary direction is
		ignored.
		"""
		if self.x_direction > 0:
			self.x_pos += self.MOVE_X_RATE
		elif self.x_direction < 0:
			self.x_pos -= self.MOVE_X_RATE

		if self.x_pos >= max_pos - self.width:
			self.x_pos = max_pos - self.width
		elif self.x_pos <= min_pos:
			self.x_pos = min_pos
	# End: def PlayerCharacter.move_x

	def move_y(self, min_pos, max_pos):
		"""
		Moves the character along its vertical plane in its current direction.
		If the character is at or past its minimum (top) or maximum (bottom)
		positional boundary then further movement in the boundary direction is
		ignored.x
		"""
		if self.y_direction > 0:
			self.y_pos += self.MOVE_Y_RATE
		elif self.y_direction < 0:
			self.y_pos -= self.MOVE_Y_RATE

		if self.y_pos >= max_pos - self.height:x
		elif self.y_pos <= min_pos:
			self.y_pos = min_pos
	# End: def PlayerCharacter.move_y
# End: class PlayerCharacter
