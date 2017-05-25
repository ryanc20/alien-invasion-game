class Settings():
	"""A class to store all settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's static settings."""
		# Screen settings
		self.screen_width = 900
		self.screen_height = 600
		self.bg_color = (230, 230, 230)

		# Ship settings
		self.ship_limit = 3

		# Bullet settings
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3

		# Alien settings
		self.fleet_drop_speed = 10

		# How quickly the game speeds uo
		self.speedup_scale = 1.15

		# How quickly the alien point values incrase
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def increase_speed(self):
		"""Increase speed settings and alien point values."""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)
		
	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game."""
		self.ship_speed_factor = .6
		self.bullet_speed_factor = 1.7
		self.alien_speed_factor = 0.4

		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1

		# Scoring
		self.alien_points = 50