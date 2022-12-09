import pygame
import util.config as cfg

from classes.game_object import GameObject

PLANE_X = 'x'
PLANE_Y = 'y'
PLANE_Z = 'z'

class MovableObject(GameObject):
	"""
	Represents an on screen movable object in the game.
	"""

	def __init__(self, data):
		"""
		Initializes a movable object with the given initialization data.

		The parameter 'data' is a map with values required by GameObject and
		additional optional values bound to the following keys:
			* 'image2'  - the optional secondary image file path to load from
						  disk.
			* 'min_xpos'- the object's optional left-most movement boundary on
						  screen
			* 'max_xpos'- the object's optional right-most movement boundary on
						  screen
			* 'min_ypos'- the object's optional top-most movement boundary on
						  screen
			* 'max_ypos'- the object's optional bottom-most movement boundary
						  on screen
			* 'speedx'  - the object's optional horizontal movement rate in
						  pixels per frame
			* 'speedy'  - the object's optional vertical movement rate in
						  pixels per frame
		"""
		super().__init__(data)
		if 'image2' in data:
			self.image2 = data['image2']
		if 'min_xpos' in data:
			self.min_xpos = data['min_xpos']
		if 'max_xpos' in data:
			self.max_xpos = data['max_xpos']
		if 'min_ypos' in data:
			self.min_ypos = data['min_ypos']
		if 'max_ypos' in data:
			self.max_ypos = data['max_ypos']
		if 'speedx' in data:
			self.MOVE_X_RATE = data['speedx']
		if 'speedy' in data:
			self.MOVE_Y_RATE = data['speedy']
		self.scr_width = cfg.get_config_value('width', 'SCREEN')
		self.scr_height = cfg.get_config_value('height', 'SCREEN')
		self.is_stopped = False
		self.is_dying = False
		self.direction_switched = False
	# End: def MovableObject.__init__

	def die(self, swap_image=False):
		"""
		Updates the object's state to dying. If 'swap_image' is True and the
		object has a secondary image then its image on screen is swapped to
		its secondary image.
		"""
		if swap_image == True and self.image2:
			self.image = pygame.transform.scale(pygame.image.load(self.image2), (self.width, self.height))
		self.is_dying = True
	# End: def MovableObject.die

	def set_movable(self, movable):
		"""
		Updates the object's movable state to the given True or False state. If
		False then the object's movement is stopped.
		"""
		self.is_stopped = not movable
	# End: def MovableObject.set_movable

	def is_movable(self):
		"""
		Returns True if the object is movable. 
		"""
		return not self.is_stopped
	# End: def MovableObject.is_active

	def switch_direction(self, movement_plane):
		"""
		Changes the object's movement direction to the opposite of its current
		direction on the specified movement plane. The specified movement_plane
		must be one of:
			* PLANE_X - horizontal movement plane
			* PLANE_Y - vertical movement plane
			* PLANE_Z - both horizontal and vertical movement planes
		"""
		if movement_plane in (PLANE_X, PLANE_Z):
			if self.MOVE_X_RATE == abs(self.MOVE_X_RATE):
				self.MOVE_X_RATE = -abs(self.MOVE_X_RATE)
			else:
				self.MOVE_X_RATE = abs(self.MOVE_X_RATE)

		if movement_plane in (PLANE_Y, PLANE_Z):
			if self.MOVE_Y_RATE == abs(self.MOVE_Y_RATE):
				self.MOVE_Y_RATE = -abs(self.MOVE_Y_RATE)
			else:
				self.MOVE_Y_RATE = abs(self.MOVE_Y_RATE)

		self.direction_switched = True
	# End: def MovableObject.switch_direction

	def move_x(self, bidirectional=True, min_pos=0, max_pos=0):
		"""
		Moves the object along its horizontal plane in its current direction
		by its set horizontal movement rate. If bidirectional movement is
		specified and the object is at or beyond its minimum or maximum
		horizontal position boundary then its direction is changed toward the
		opposite boundary. Otherwise, the object's horizontal movement is
		stopped once it reaches its targeted boundary or is in dying state.
		"""
		if self.min_xpos and min_pos == 0:
			min_pos = int(self.min_xpos)
		if self.max_xpos and max_pos == 0:
			max_pos = int(self.max_xpos)

		if not self.is_stopped and not self.is_dying:
			if bidirectional:
				self.direction_switched = False
				if self.x_pos <= min_pos or self.x_pos >= max_pos-self.width:
					self.switch_direction(PLANE_X)
			self.x_pos += self.MOVE_X_RATE
			self.is_stopped = (not bidirectional and (self.x_pos <= min_pos or self.x_pos >= max_pos-self.width))
		if self.is_dying:
			self.is_stopped = True
	# End: def MovableObject.move_x

	def move_y(self, bidirectional=True, min_pos=0, max_pos=0):
		"""
		Moves the object along its vertical plane in its current direction by
		its set vertical movement rate. If bidirectional movement is specified
		and the object is at or beyond its minimum or maximum vertical position
		boundary then its direction is changed toward the opposite boundary.
		Otherwise, the object's vertical movement is stopped once it reaches
		its targeted boundary or is in dying state.
		"""
		if self.min_ypos and min_pos == 0:
			min_pos = int(self.min_ypos)
		if self.max_ypos and max_pos == 0:
			max_pos = int(self.max_ypos)

		if not self.is_stopped and not self.is_dying:
			if bidirectional:
				self.direction_switched = False
				if self.y_pos <= min_pos or self.y_pos >= max_pos-self.height:
					self.switch_direction(PLANE_Y)
			self.y_pos += self.MOVE_Y_RATE
			self.is_stopped = (not bidirectional and (self.y_pos <= min_pos or self.y_pos >= max_pos-self.height))
		if self.is_dying:
			self.is_stopped = True
	# End: def MovableObject.move_x
# End: class MovableObject
