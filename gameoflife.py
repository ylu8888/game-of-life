# Name: Yang Lu
# This project is due by Nov. 30 at 11:59pm.
# Follow the instructions for Steps 1–10 below. Upload your file to Brightspace when it is complete.

import time
import random
from graphics import *

# This creates a text-based version of the game.

def create_row(n):
   row = []
   for i in range(n):
       row.append(' ')
   return row

# Note: This corresponds to exercise 10.3 in the textbook.

def create_grid(rows, cols):
    grid = []

    for r in range(rows):
        grid.append(create_row(cols))

    return grid

# Note: This corresponds to exercise 10.6 in the textbook.

def populate(grid, prob):
    rows = len(grid)
    cols = len(grid[0])
## Step 1: for loop syntax.
    # On the blank line below, write a for statement that iterates variable r over the range specified by rows. (Note: rows is already defined above.)
    # Note: Make sure that the statement is properly indented. Your first for statement should line up with the hashtag at the beginning of this line.
    # Then write an inner loop that iterates variable c over the range specified by cols. (Note: cols is already defined above.)
    
    for r in range(rows):
        for c in range(cols):    
            if random.random() <= prob:
                grid[r][c] = '*'
            else:
                grid[r][c] = ' '
                
# Note: This corresponds to exercise 10.7 in the textbook.

def neighbors(grid, row, column):
    total = 0
    
    height = len(grid)
    width = len(grid[0])
## Step 2 & 3: for loop syntax cont.
    # On the line below, write a for statement that iterates variable x over the range between row minus one and row plus 2.
    # Then write an inner loop that iterates variable y over the range between column minus one and column plus 2.
    # Note: make sure that your first for statement is properly indented. It should align with the hashtag at the beginning of this line.
    for x in range(row - 1, row + 2):
        for y in range(column - 1, column + 2):
        
            ## On the blank line below, write a statement that specifies the following:
            ## if x is less-than zero OR x is greater-than-or-equal-to height OR y is less than zero OR y is greater-than-or-equal-to width then:
            ## Note: your statement should align with the hashtag at the beginning of this line.
            if(x < 0 or x >= height or y < 0 or y >= width):
                continue
            ## On the blank line below, write a statement that specifies the following:
            ## If x is equal to row AND y is equal to column then:
            ## Note: your statement should align with the hashtag at the beginning of this line.
            
            if(x == row and y == column):
                continue
            if grid[x][y] == '*':
                total += 1
    return total


# Note: This corresponds to exercise 10.9 in the textbook.

def evolve(grid):
    rows = len(grid)
    cols = len(grid[0])

    new_grid = create_grid(rows, cols)

## Steps 4, 5, and 6: Specifying the rules of the game.   
    # On the blank line below, write a for statement that iterates variable r over the range specified by rows. (Note: rows is already defined above.)
    # Note: Make sure that the statement is properly indented. Your first for statement should line up with the hashtag at the beginning of this line.
    # Then write an inner loop that iterates variable c over the range specified by cols. (Note: cols is already defined above.)   
    
    for r in range(rows):
        for c in range(cols):
            n = neighbors(grid, r, c)
            if grid[r][c] == '*':
                # Write a statement that specifies if n is equal to two OR is equal to three, then:
                if n == 2 or n == 3:
                    new_grid[r][c] = '*'  # Cell stays alive
                else:
                    new_grid[r][c] = ' '  # Cell dies
            else:
                # Write a statement that specifies if n is equal to three, then: 
                if n == 3:
                    new_grid[r][c] = '*'  # Cell becomes alive
                else:
                    new_grid[r][c] = ' '  # Cell stays dead
    return new_grid


grid = create_grid(50,50)


for generation in range(500):
    grid = evolve(grid)

# Note: This corresponds to exercise 10.9 in the textbook.


def create_grid_visual(rows, cols, window):
    grid_visual = create_grid(rows, cols)

    p_w = window.getWidth() // cols # pixel wideth
    p_h = window.getHeight() // rows # pixel height

## Step 7: for loop syntax.
    # On the blank line below, write a for statement that iterates variable r over the range specified by rows. (Note: rows is already defined above.)
    # Note: Make sure that the statement is properly indented. Your first for statement should line up with the hashtag at the beginning of this line.
    # Then write an inner loop that iterates variable c over the range specified by cols. (Note: cols is already defined above.)
    
    for r in range(rows):
        for c in range(cols):
        
           grid_visual[r][c] = Rectangle(Point(c*p_w, r*p_h), Point((c+1)*p_w, (r+1)*p_h))
           grid_visual[r][c].setFill(color_rgb(0,0,0))
           grid_visual[r][c].draw(window)
    return grid_visual

# Note: This corresponds to exercise 10.9 in the textbook.

## Step 8: for loop syntax

def mirror(grid, grid_visual):
    rows = len(grid)
    cols = len(grid[0])
    # On the line below, write a for statement that iterates variable r over the range specified by rows. (Note: rows is already defined above.)
    # Note: Make sure that the statement is properly indented. Your first for statement should line up with the hashtag at the beginning of this line.
    # Then write an inner loop that iterates variable c over the range specified by cols. (Note: cols is already defined above.)
    for r in range(rows):
        for c in range(cols):
        
            if grid[r][c] == '*':
## Step 9: The line below specifies the color of your living cells.
##         Manipulate the R,G,B values so that your living cells are purple.
                grid_visual[r][c].setFill(color_rgb(128,0,128)) # This starting color is green. What are the R,G,B values for purple?
            else:
                grid_visual[r][c].setFill(color_rgb(0,0,0))
                
                                         
window = GraphWin('Game of Life', 500, 500, autoflush=False)
grid = create_grid(50,50)
grid_visual = create_grid_visual(50,50,window)
populate(grid,0.3)
## Step 10: The line above sets the initial state of the game.
#          This function tells Python to populate grid in such a way that each call has a 50% chance
#          of being alive in the initial state. Run the program and make a note to yourself about the
#          population density at the start of the game. The initial chance rate is indicated by the second
#          input: .5. Try retuning the initial rate and see what happens. Make a note to yourself.
#          Before you submit this assignment to Brightspace, set the input so that each cell has a
#          30% chance of being alive in the initial state.

# The line below indicates the range of generations through which the game will iterate.
# Currently, the game is set to run through 500 generations. If you want to see what happens
# with different numbers of generations, you can change the range from 500 to a different
# number. However, before you submit the assignment to Brightspace, make sure that the generation range
# is are set back to 500.
for generation in range(500):
    mirror(grid, grid_visual)
    window.update()
    grid = evolve(grid)
    time.sleep(0.25)

# In case you want to play around with it further!:
# The time.sleep(0.5) statement above sets the speed of each generation.
# Currently, the game will iterate through a generation in .5 seconds.
# If you want to slow the game down, you can make the number bigger.
# For instance, time.sleep(1) will give you one second between each generation.
# If you want to speed it up, you can make the number smaller.
# For instance, time.sleep(.25) will give you .25 seconds between each generation.



