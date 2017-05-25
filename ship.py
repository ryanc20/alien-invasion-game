import pygame
from pygame.sprite import Sprite 

def load_image(path):
	"""Load the image and store into the image variable."""
	image = pygame.image.load(path)
	return image

class Ship(Sprite):

	def __init__(self, ai_settings, screen):
		"""Initialize the ship and set its starting position."""
		super(Ship, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		# Load the ship images and get its rect.
		self.images = []
		self.images.append(load_image('images/ship_red.png'))
		self.images.append(load_image('images/ship_green.png'))
		self.images.append(load_image('images/ship_blue.png'))
		self.images.append(load_image('images/ship_yellow.png'))
		self.index = 0
		self.image = self.images[self.index]
		self.rect = pygame.Rect(0, 0, 64, 64)

		self.screen_rect = screen.get_rect()

		# Start each new ship at the bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# Store a decimal value for the ship's center.
		self.center = float(self.rect.centerx)

		# Movement flag
		self.moving_right = False
		self.moving_left = False

	def center_ship(self):
		"""Center the ship on the screen."""
		self.center = self.screen_rect.centerx

	def update(self):
		"""
			Update the ship image creating animation.
			Update the ship's position based on the movement flag.
		"""
		# Animation for the ship to change colors!
		for count in range(1000):
			if count == 999:
				self.index +=1
				if self.index >= 3:
					self.index = 0
				self.image = self.images[self.index]
				count = 0
			else:
				count += 1

		# Update the ship's center value, not the rect.
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor

		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor

		# Update rect object
		self.rect.centerx = self.center

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)