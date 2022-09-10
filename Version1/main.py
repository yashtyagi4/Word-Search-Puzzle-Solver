# Yash Tyagi
# Project: Word Search Solver
# main.py purpose: 1) Ask user to imput words and the grid
#                  2) Runs the Solver

from solver import Solver


def main():
    # Inputting Rows and Cols from User
    rows = 0
    cols = 0
    while (rows <= 0):
        rows = int(input("Enter number of rows: "))
        if (rows <= 0):
            print("Sorry, no rows at or below zero!")
    while (cols <= 0):
        cols = int(input("Enter number of columns: "))
        if (cols <= 0):
            print("Sorry, no columns at or below zero!")
    grid = [[""]*cols]*rows # Setting up the grid


    # Filling the Grid
    print("\nTime to Input the Grid!")
    for i in range (0, rows):
        gridRow = ""
        while (len(gridRow) != cols):
            gridRow = input("Enter Complete Row " + str(i+1) + " in a string format (example: abcdefg): ")
            if (len(gridRow) != cols):
                print("Enter right number of elements in the row!")
                continue
        grid[i] = list(gridRow)


    # Filling list of Words
    print("\nTime to Input the words to be found!")
    numWords = 0
    while(numWords <= 0):
        numWords = input("Enter the number of words to be found in the grid: ")
        numWords = int(numWords)
        if (numWords <= 0):
            print("Sorry, number of words can't be less than zero!")
    words = [""]*numWords
    for i in range(numWords):
        words[i] = input("Enter Word " + str(i+1) + ": ")

    # Calling the Grid Solver
    moves = Solver(grid, words)
    
    #Printing the moves
    for word, move in moves.items():
        print(word, ' : ', move)


if __name__ == "__main__":
    main()