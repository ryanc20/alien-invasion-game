# Alien Invasion

Alien Invasion is a game written in Python that is a clone of the popular Space Invader games from ancient times.

## Example of Code

```python
def store_high_score(stats):
	"""Store the high score into a text file."""
	filename = 'high_score.txt'

	with open(filename, 'w') as file_object:
		hs = str(stats.high_score)
		file_object.write(hs)
```
The above code shows the process for storing the high score into a text file.

## Motivation

I am fascinated by the process of creating games and managing everything to create a final product. I wanted to become more exposed to using Python and I thought making a game would be a great way to bind two of my interests into a rewarding experience.

## How to Run

Download the repository (assuming Python and the Pygame library are installed) and run the alien_invasion.py file.

## Note

The game was completed following a tutorial from the book [Python Crash Course: A Hands-On, Project-Based Introduction to Python by Eric Matthes.](https://www.amazon.com/Python-Crash-Course-Hands-Project-Based/dp/1593276036/ref=sr_1_1?ie=UTF8&qid=1495703885&sr=8-1&keywords=python+crash+course) I was able to complete the game following the instruction of the book and have added improvements to the game to practice using Python and Python libraries.

The current version is incomplete and I plan to make several changes such as:
- Storing the High Score to be saved even when the game is exited. (Completed)
- Animation of the ship and aliens. (Completed 50%)
- Audio for the bullets and background music.
- At the end of the game I would like to display stats such as accuracy and aliens destroyed.
- Improve the graphics and finetune the gameplay.
- Creating a Start Menu with graphics.
- etc.

(If you couldn't tell I am also practicing how to format and write README.md files)
