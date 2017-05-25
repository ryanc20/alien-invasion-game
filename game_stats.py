class GameStats():
	"""Track statistics for Alien Invasion."""
	def __init__(self, ai_settings):
		"""Initialize statistics."""
		self.ai_settings = ai_settings
		self.reset_stats()

		# Start Alien Invasion in an inactive state.
		self.game_active = False

		# High score is loaded from file, unless file doesn't exist.
		try:
			self.read_high_score()
		except FileNotFoundError:
			self.high_score = 0

	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1

	def read_high_score(self):
		"""Read high score from textfile."""
		with open('high_score.txt') as file_object:
			self.high_score = int(file_object.read())
