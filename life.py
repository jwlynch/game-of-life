"""Conway's Game of Life, by Al Sweigart al@inventwithpython.com
The classic cellular automata simulation. Press Ctrl-C to stop.
More info at" https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
View this code at https://nostarch.com/big-book-of-small-python-projects
Tags" short, artistic, simulation"""

import copy, random, sys, time

# Set up the constants:
WIDTH = 79  # The width of the cell grid.
HEIGHT = 20 # The height of the cell grid.

# (!) Try changing ALIVE to '#' or another character:
ALIVE = 'O'  # The character representing a living cell.
# (!) Try changing DEAD to '.' or another character:
DEAD = ' '   # The character representing a dead cell.

# Try changing ALIVE to '|' and DEAD to '-'.

# The cells and nextCells are dictionaries for the state of the game.
# Their keys are (x, y) tuples and their values are one of the ALIVE
# or DEAD values.
nextCells = {}
