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
# put random dead and live cells into nextCells:
for x in range(WIDTH):  # loop over every possible column.
    for y in range(HEIGHT):  # loop over every possible row.
        # 50/50 chance for starting cells being alive or dead.
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = ALIVE # Add a living cell.
        else:
            nextCells[(x, y)] = DEAD  # Add a dead cell.

while True:

    for x in range(WIDTH):
        for y in range(HEIGHT):
    try:
        time.sleep(1) # Add a 1 second pause to reduce flickering.
    except KeyboardInterrupt:
        print("Conway's Game of Life")
        print("by Al Sweigart al@inventwithpython.com")
        sys.exit()  # When Ctrl-C is pressed, end the program.
