# Alien Invasion

Alien Invasion is a game written in Python that is a clone of the popular Space Invader games from ancient times.

# Example of Code

```python
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	"""Create an alien and place it in the row."""
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width	
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)
```
The above code shows the process for creating an alien and adding it to the row of aliens.

# Motivation

I am fascinated by the process of creating games and managing everything to create a final product. I wanted to become more exposed to using Python and I thought making a game would be a great way to bind two of my interests into a rewarding experience.

# How to Run

Download the repository (assuming Python and the Pygame library are installed) and run the alien_invasion.py

# Note

The game was completed following a tutorial from the book [Python Crash Course: A Hands-On, Project-Based Introduction to Python by Eric Matthes.](https://www.amazon.com/Python-Crash-Course-Hands-Project-Based/dp/1593276036/ref=sr_1_1?ie=UTF8&qid=1495703885&sr=8-1&keywords=python+crash+course) I was able to complete the game following the instruction of the book and have added improvements to the game to practice using Python and Python libraries.

The current version is incomplete and I plan to make several changes such as:
- Storing the High Score to be saved even when the game is exited.
- Animation of the ship and aliens.
- Audio for the bullets and background music.
- At the end of the game I would like to display stats such as accuracy and aliens destroyed.
- Improve the graphics and finetune the gameplay.
- Creating a Start Menu with graphics.
- etc.

(If you couldn't tell I am also practicing how to format and write README.md files)
