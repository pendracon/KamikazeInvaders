#!/usr/bin/python3
"""
Kamikaze Invaders: a 'Space Invaders' and 'Galaga' inspired game developed
with PyGame.
"""
import pygame

import util.config as cfg

from classes.game_object import GameObject
from classes.movable_object import MovableObject, PLANE_Y
from classes.character import EnemyCharacter, PlayerCharacter
from classes.ui import QuitOrStartPanel, CLR_WHITE

class KamikazeInvaders:
	def __init__(self):
		# Initialize resources
		pygame.init()
		pygame.font.init()
		self.FONT1 = pygame.font.SysFont('comicsans', 52)
		self.FONT2 = pygame.font.SysFont('comicsans', 36)
		self.CLOCK_RATE = int(cfg.get_config_value('framerate', 'SCREEN'))
		self.game_objects = {'player': None, 'helper': None, 'enemies': [], 'bullets': [], 'powerups': []}
		self.max_bullets = 1

		# Set up the main screen
		pygame.display.set_caption(cfg.get_config_value('title', 'META'))
		self.width = int(cfg.get_config_value('width', 'SCREEN'))
		self.height = int(cfg.get_config_value('height', 'SCREEN'))
		self.main_screen = pygame.display.set_mode((self.width, self.height))
		self.background = GameObject({
			'image': cfg.get_config_value('background', 'SCREEN'),
			'xpos': 0,
			'ypos': 0,
			'iwidth': self.width,
			'iheight': self.height
			})
		
		# Set up supporting UI elements
		self.quit_or_start_panel = QuitOrStartPanel(self.main_screen, self)
	# End: def KamikazeInvaders.__init__

	def run(self):
		# Initialize game objects
		player = PlayerCharacter(get_object_data('player'))
		self.game_objects['player'] = player
		self._reset(player)

		# Play!
		self.clock = pygame.time.Clock()
		DO_LOOP = True
		while DO_LOOP:
			DO_LOOP = self._check_events(player)
			if DO_LOOP:
				DO_LOOP = not self._refresh(self.game_objects)
				self._update(self.CLOCK_RATE)
			if not DO_LOOP:
				DO_LOOP = self.quit_or_start_panel.show(player)

		# That's all folks!
		pygame.quit()
	# End: def KamikazeInvaders.run

	def _reset(self, player):
		player.reset()
		self.max_bullets = 1
		self.game_objects['enemies'] = self._spawn_enemies(player.get_ypos()+player.get_height())
		self.game_objects['helper'] = None
		self.game_objects['bullets'] = []
		self.game_objects['powerups'] = []
	# End: KamikazeInvaders._reset

	def _spawn_enemies(self, max_ypos):
		"""
		Creates the enemies to shoot and spawns them at the top of the screen.
		"""
		enemies = {'beige': [], 'green': [], 'pink': [], 'yellow': [], 'blue': []}
		ypos = 10
		for enemy_type in enemies:
			data = get_object_data(f'{enemy_type}Enemy')
			enemy_width = int(data['iwidth'] * 1.5)
			total_width = enemy_width * 10
			xpos = (self.width - total_width) // 2
			movement = xpos - 10
			for i in range(10):
				data['xpos'] = xpos
				data['ypos'] = ypos
				data['min_xpos'] = xpos - movement
				data['max_xpos'] = xpos + enemy_width + movement
				data['max_ypos'] = max_ypos
				enemy = EnemyCharacter(data.copy())
				enemies[enemy_type].append(enemy)
				xpos += enemy_width
			ypos = data['ypos'] + data['iheight'] + 10

		return enemies
	# End: def KamikazeInvaders._spawn_enemies

	def _fire_weapon(self, player, bullets):
		"""
		Fires a bullet from the player character's current location toward the
		top of the screen. The call is ignored if a bullet is currently in
		play.
		"""
		if len(bullets) < self.max_bullets:
			xpos = player.get_xpos() + (player.get_width() // 2)
			data = get_object_data('bullet')
			data['xpos'] = xpos
			data['ypos'] = player.get_ypos()
			data['min_ypos'] = 0
			data['max_ypos'] = self.height
			bullet = MovableObject(data)
			bullet.switch_direction(PLANE_Y)
			bullets.append(bullet)
	# End: def KamikazeInvaders._fire_weapon

	def _is_hit(self, enemy, bullets):
		"""
		Returns True if the given enemy is collided with a bullet.
		"""
		enemy_hit = False

		for bullet in bullets:
			if enemy.is_collided(bullet):
				enemy_hit = True
				bullets.remove(bullet)
				break
		
		return enemy_hit
	# End: def KamikazeInvaders._is_hit

	def _check_events(self, player, end_loop=False):
		is_running = not end_loop
		fire_weapon = False

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				if end_loop:
					is_running = True
				else:
					is_running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					player.set_x_direction(1)
				elif event.key == pygame.K_LEFT:
					player.set_x_direction(-1)
				elif event.key == pygame.K_SPACE:
					if end_loop:
						fire_weapon = True
					else:
						self._fire_weapon(player, self.game_objects['bullets'])
				elif event.key == pygame.K_q:
					if end_loop:
						is_running = True
					else:
						is_running = False
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
					player.set_x_direction(0)

		if end_loop:
			return is_running, fire_weapon
		else:
			return is_running
	# End: def KamikazeInvaders._check_events
 
	def _update(self, wait_time):
		pygame.display.update()
		self.clock.tick(wait_time)
	# End: def KamikazeInvaders._update

	def _refresh(self, game_objects):
		self.main_screen.fill(CLR_WHITE)
		self.background.draw(self.main_screen)

		end_game = False
		player = game_objects['player']

		for bullet in game_objects['bullets']:
			bullet.move_y(0, False)
			if not bullet.is_movable():
				game_objects['bullets'].remove(bullet)
			else:
				bullet.draw(self.main_screen)

		for enemy_color in game_objects['enemies']:
			enemies = game_objects['enemies'][enemy_color]
			for enemy in enemies:
				if not enemy.is_movable():
					enemies.remove(enemy)
				else:
					if self._is_hit(enemy, game_objects['bullets']):
						enemy.die(True)
					else:
						enemy.move_x()
						if enemy.is_collided(player):
							enemy.die(True)
							player.die(True)
							end_game = True
					enemy.draw(self.main_screen)

		if player.is_movable():
			player.move_x(10, self.width-10)
		player.draw(self.main_screen)

		return end_game
	# End: def KamikazeInvaders._refresh
# End: class KamikazeInvaders


def get_object_data(key_type, index=1, max=1):
	data = {}
	data['image'] = cfg.get_config_value(f'{key_type}Image', 'OBJECTS')
	data['image2'] = cfg.get_config_value(f'{key_type}Image2', 'OBJECTS')
	data['iwidth'] = int(cfg.get_config_value(f'{key_type}ImageW', 'OBJECTS'))
	data['iheight'] = int(cfg.get_config_value(f'{key_type}ImageH', 'OBJECTS'))
	data['speedx'] = int(cfg.get_config_value_default(f'{key_type}SpeedX', 'OBJECTS', 0))
	data['speedy'] = int(cfg.get_config_value_default(f'{key_type}SpeedY', 'OBJECTS', 0))
	data['points'] = int(cfg.get_config_value_default(f'{key_type}Points', 'OBJECTS', 0))

	width = int(cfg.get_config_value('width', 'SCREEN'))
	height = int(cfg.get_config_value('height', 'SCREEN'))
	data['xpos'] = (width - data['iwidth']) // 2
	data['ypos'] = height - data['iheight'] - (data['iheight'] // 2)

	return data
# End: def get_object_data


# Get the show on the road!
if __name__ == '__main__':
	config = cfg.IniConfig('config/game.ini')
	game = KamikazeInvaders()
	game.run()
	quit()
