ALIEN_X_LEN = 12
ALIEN_Y_LEN = 7

aliens = {}
aliens_green = []
aliens_blue = []
aliens_red = []
aliens['green'] = aliens_green
aliens['blue'] = aliens_blue
aliens['red'] = aliens_red

green_alien = {'color': 'green', 'points': 5}
blue_alien = {'color': 'blue', 'points': 10}
red_alien = {'color': 'red', 'points': 15}

for i in range(10):
	# Add green alien
	alien = green_alien.copy()
	alien['x_pos'] = (i * ALIEN_X_LEN) + ALIEN_X_LEN
	alien['y_pos'] = ALIEN_Y_LEN * 1
	aliens_green.append(alien)

	# Add blue alien
	alien = blue_alien.copy()
	alien['x_pos'] = (i * ALIEN_X_LEN) + ALIEN_X_LEN
	alien['y_pos'] = ALIEN_Y_LEN * 2
	aliens_blue.append(alien)

	# Add red alien
	alien = red_alien.copy()
	alien['x_pos'] = (i * ALIEN_X_LEN) + ALIEN_X_LEN
	alien['y_pos'] = ALIEN_Y_LEN * 3
	aliens_red.append(alien)

for color in aliens.keys():
	print(f"{color.title()} alien positions:")
	positions = []
	for alien in aliens[color]:
		positions.append(f"{alien['x_pos']},{alien['y_pos']}")
	print(f"\t{positions}\n")
