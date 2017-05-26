import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to manage bullets fired from the ship"""
	
	def __init__(self, ai_settings, screen, ship):
		"""Create a bullet object at the ship's current position."""
		super(Bullet, self).__init__()
		self.screen = screen

		# Create a bullet rect at (0, 0) then set correct position.
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, 
			ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		# Store the bullet's position as a decimal value
		self.y = float(self.rect.y)

		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor

	def update(self, ai_settings):
		"""Move the bullet up the screen and change colors."""
		
		for count in range(10):
			if count == 9:
				ai_settings.index += 1
				if ai_settings.index >= 3:
					ai_settings.index = 0
				ai_settings.bullet_color = ai_settings.bullet_colors[ai_settings.index]
				count = 0
			else:
				count += 1


		# Update the decimal position of the bullet.
		self.y -= self.speed_factor
		# Update the rect position
		self.rect.y = self.y

	def draw_bullet(self):
		"""Draw the bullet to the screeen."""
		pygame.draw.rect(self.screen, self.color, self.rect)