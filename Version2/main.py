# Yash Tyagi
# Project: Word Search Solver
# Version 2 Purpose: Furthur develop Version 1 to implement
#                    Selenium WebDriver so that the solver
#                    can find a word puzzle by itself and
#                    solve it on the screen

import time
from solver import Solver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import solver


def main():

    # Ask User Options
    while (True):
        option = input("Select an option: \nEnter 1 to run the bot that plays on web.\nEnter 2 to fill the grid and give the words to find manually.\nEnter here: ")
        if (option == "1" or option == "2"):
            break
        else:
            print("Wrong Input! Enter correct number.")

    # Perform the right option
    if (option == "1"): bot(option)
    else: manual(option)

def bot(option):
    # Opening game website
    driver = webdriver.Chrome(executable_path=r'/Users/yashtyagi/Git/Word-Search-Puzzle-Solver/chromedriver')
    driver.maximize_window()
    driver.get('https://wordsearch.samsonn.com/')
    time.sleep(2)


    # Setting up the grid
    rows = 15
    cols = 15
    grid = [['']*rows for _ in range(cols)]

    # Filling the grid
    for row in range(rows):
        for col in range(cols):
            # From Chrome developor tools we extracted the class containing the grid and then the cell containing the value at i,j
            cell = driver.find_element(by=By.XPATH, value=f'//div[@class="Grid_gridCell__1L1O2" and @row={row} and @col={col}]')
            grid[row][col] = cell.text
    
    # Get the words
    word_list = driver.find_element(by=By.XPATH, value='//*[@id="App"]/div[2]/div/div/div[2]')  
    # Single word inside the class is of type a so we find all elements of type a in the words list (class) and put their text in a set of words   
    words = set([word.text for word in word_list.find_elements(by=By.XPATH, value='//a')])

    # Calling Solver
    moves = Solver(grid, words, option, driver)

    #Printing the moves
    for word, move in moves.items():
        if (move != None):   
            print(word, ' : ', move)
        
    time.sleep(2)
    # To switch the focus to alerts
    driver.switch_to.alert.dismiss()
    time.sleep(10)


def manual(option):
    driver = None
    if (option == 1):
        driver = webdriver.Chrome(driver = webdriver.Chrome(executable_path=r'/Users/yashtyagi/Git/Word-Search-Puzzle-Solver/chromedriver'))

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
    moves = Solver(grid, words, option, driver)
    
    # Printing the moves
    for word, move in moves.items():
            print(word, ' : ', move)


if __name__ == "__main__":
    main()