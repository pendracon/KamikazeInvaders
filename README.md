# Kamikaze Invaders
**Under Development**
A Galaga and Space Invaders inspired 2D game in Python using Pygame.

## Overview
In Kamikaze Invaders, the player controls a space ship that appears at the
bottom center of the screen. The player can move the ship right and left using
the arrow keys and shoot at enemies using the spacebar. Only one shot at a time
is possible in normal play, i.e. while one shot is in play the player can not
fire another shot until the current shot either hits an enemy or reaches the
top of the screen.

Rows of different colored enemy space ships fill the top of the screen and
slowly move back and forth across it. Each enemy in the fleet has a left
and right movement limit defined by their initial relative position on screen.
As the enemies reach their movement limits on either side they drop down
closer to the player's ship.

If an enemy ship reaches the bottom of the screen normally and collides with
the player's ship, both the enemy and player ships are destroyed with no points
awarded to the player. At random intervals, enemy ships attempt to kamikaze
'dive bomb' the player's ship by quickly descending to the player's row while
continuing to oscillate. If a dive-bombing enemy ship collides with the
player's ship, both the enemy ship and player's ship are destroyed but the
enemy's point value is awarded to the player.

A "supply" ship can occasionally appear and move once across the game screen.
When this happens the ship will drop one of the following "power ups" for the
player to "catch":

* Shot power up - allows the player to shoot extra shots for a short amount of
  time.
* Ship power up - makes the player's ship indestructable for short amount of
  time.
* Life power up - awards an extra ship to the player.

## Playing
When the game begins, a fleet of aliens fills the sky and moves across and down
the screen. The player shoots and destroys the aliens. If all enemy ships in a
fleet are destroyed, a new fleet appears that moves faster than the previous
fleet. If any alien hits the player’s ship after reaching the bottom or by
kamikaze dive-bombing the player, the player loses a ship. If all of the
player's ships are destroyed, the game ends.

## Attributions
Background image by <a href="https://www.freepik.com/free-vector/cartoon-galaxy-background-with-planets_14121184.htm#query=space%20background&position=37&from_view=keyword">Freepik</a>
