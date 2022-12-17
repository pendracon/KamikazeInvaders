import pygame

class GameObject:
	"""
	Represents an on screen object in the game with collision detection.
	"""
	def __init__(self, data):
		"""
		Initializes the object by loading its image file from the given file
		system path and setting its x and y pixel positions on screen, and the
		pixel width and height of its on screen image ("sprite").

		The parameter 'data' is a map with the required values bound to the
		following keys:
			* 'image'   - the image file path to load from disk.
			* 'xpos'    - the image's x-coordinate on screen
			* 'ypos'    - the image's y-coordinate on screen
			* 'iwidth'  - the image width in pixels
			* 'iheight' - the image height in pixels
		"""
		self.image1 = data['image']
		self.starting_x_pos = data['xpos']
		self.starting_y_pos = data['ypos']
		self.width = data['iwidth']
		self.height = data['iheight']
		self.reset()
	# End: def GameObject.__init__

	def is_collided(self, object):
		"""
		Tests whether this object is collided with the given object. Returns
		True if collided, otherwise returns False.
		"""
		collided = True

		if self.y_pos + self.height < object.y_pos or self.y_pos > object.y_pos + object.height:
			collided = False
		elif self.x_pos + self.width < object.x_pos or self.x_pos > object.x_pos + object.width:
			collided = False
		
		return collided
	# End: def GameObject.is_collided

	def get_xpos(self):
		"""
		Returns the object's current x coordinate on screen.
		"""
		return self.x_pos
	# End: def GameObject.get_xpos
	
	def get_ypos(self):
		"""
		Returns the object's current y coordinate on screen.
		"""
		return self.y_pos
	# End: def GameObject.get_ypos

	def get_width(self):
		"""
		Returns the object's surface width in pixels.
		"""
		return self.width
	# End: def GameObject.get_width
	
	def get_height(self):
		"""
		Returns the object's surface height in pixels.
		"""
		return self.height
	# End: def GameObject.get_height
	
	def draw(self, surface):
		"""
		Displays the object on the given screen surface.
		"""
		surface.blit(self.image, [self.x_pos, self.y_pos])
	# End: def GameObject.draw

	def reset(self):
		"""
		Resets the object's location on screen to it's original x and y pixel
		positions.
		"""
		self.image = pygame.transform.scale(pygame.image.load(self.image1), (self.width, self.height))
		self.x_pos = self.starting_x_pos
		self.y_pos = self.starting_y_pos
	# End: def GameObject.reset
# End: class GameObject
