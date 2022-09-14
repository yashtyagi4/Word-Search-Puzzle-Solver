# Yash Tyagi
# Project: Word Search Solver
# solver.py purpose: Contains the Solver function and a Checker function
#                    which is utilized by the Solver

from tracemalloc import start
import trie

def Solver (grid, strings):
    words = trie.Trie().build(strings)     # Storing words in Trie DS for efficiency
    moves = dict.fromkeys(strings, None) # Store the moves for each word

    directions = [( 0, 1),(1, 1),(1, 0),( 1,-1),( 0,-1),
                  (-1,-1),(-1,0),(-1,1),(-1, 0),(-1, 1)]

    # Grid Dimensions
    rows = len(grid)
    cols = len(grid[0])

    # At each possible cell we will check for combination in each direction
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] in words.children: 
                for i_change, j_change in directions:
                    Checker(grid, words, rows, cols, i, j, i_change, j_change, moves)
    return moves


def Checker(grid, words, rows, cols, i, j, i_change, j_change, moves):
    combination = ""           #Combination being formned on the grid
    currentChar = words        #Current character node to be checked on the Trie 
    start_i = i
    start_j = j


    while (0 <= i and i < rows and 0 <= j and j < cols and
            grid[i][j] in currentChar.children):
        # currentChar becomes the currentChar children that matches the grid character i,j
        currentChar = currentChar.children[grid[i][j]] 
        combination += grid[i][j] # Adding the grid character to the combination formed

        if(currentChar.is_end):
            moves[combination] = {(start_i, start_j), (i, j)} #store the moves for the words
            words.delete(combination)   #delete the word from the list

        #Updating i, j based on the direction
        i += i_change
        j += j_change