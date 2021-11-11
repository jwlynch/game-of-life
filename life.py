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

while True:  # Main program loop.
    # Each iteration of this loop is a step of the simulation.

    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get the neighboring coordinates of (x, y), even if they
            # wrap around the edge:
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            # Count the number of living neighbors:
            numNeighbors = 0
            if cells[(left, above)] == ALIVE:
                numNeighbors += 1  # Top-left neighbor is alive
            if cells[(x, above)] == ALIVE:
                numNeighbors += 1  # Top neighbor is alive
            if cells[(right, above)] == ALIVE:
                numNeighbors += 1  # Top-right neighbor is alive
            if cells[(left, y)] == ALIVE:
                numNeighbors += 1  # Left neighbor is alive
            if cells[(right, y)] == ALIVE:
                numNeighbors += 1  # Right neighbor is alive
            if cells[(left, below)] == ALIVE:
                numNeighbors += 1  # Bottom-left neighbor is alive
            if cells[(x, below)] == ALIVE:
                numNeighbors += 1  # Bottom neighbor is alive
            if cells[(right, below)] == ALIVE:
                numNeighbors += 1  # Bottom-right neighbor is alive

    try:
        time.sleep(1) # Add a 1 second pause to reduce flickering.
    except KeyboardInterrupt:
        print("Conway's Game of Life")
        print("by Al Sweigart al@inventwithpython.com")
        sys.exit()  # When Ctrl-C is pressed, end the program.
