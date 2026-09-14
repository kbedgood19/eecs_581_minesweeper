"""
Description: Handles the command line interface game loop and user input. Displays the board, validates player moves, and sends uncover or flag actions
to the game logic.
Inputs: Number of mines (10-20), column (A-J), row (1-10), and action (U or F).
Outputs: Displays the 10x10 game board, game status, and final win or loss message.

Author: Sabelli Antebi
Creation Date: 09-13-2026
External Sources: https://www.askpython.com/python/examples/create-minesweeper-using-python used this to help me clear some of my doubts a
nd ideas a little better. 
"""

from game_logic import GameLogic
from board_manager import BoardManager

def display_board(board: BoardManager) -> None:

    print("\n    A   B   C   D   E   F   G   H   I   J") #print the column letters
    print("   +---+---+---+---+---+---+---+---+---+---+") #print the top border of the board

    for row in range(board.rows): #go through each row in the board
        print(str(row + 1).rjust(2) + " |", end="") #print the row number and keep printing on the same line
        for col in range(board.cols): #go through each column in the current row
            cell = board.get_cell(row, col) #get the current cell from the board
            if cell.state == 0: #check if the cell is covered
                symbol = "#" #use # to show a covered cell
            elif cell.state == 1: #check if the cell is flagged
                symbol = "F" #use F to show a flagged cell
            elif cell.state == 2: #check if the cell is uncovered
                if cell.adjacent_mines == 0: #check if there are no mines around the cell
                    symbol = " " #show an empty space if there are no nearby mines
                else: #if there are mines around the cell
                    symbol = str(cell.adjacent_mines) #show the number of nearby mines
            elif cell.state == 3: #check if the cell is a mine
                symbol = "*" #use * to show a mine
            else: #handle any unexpected cell state
                symbol = "?" #show ? if the cell state is not recognized

            print(" " + symbol + " |", end="") #print the current cell symbol
            
        print() #move to the next line after finishing the row

        print("   +---+---+---+---+---+---+---+---+---+---+") #print the border under the row

def main():
    board = BoardManager() #create the 10x10 board

    while True: #keep asking until the user enters a valid mine number

        try: #try to convert the input into an integer
            num_mines = int(input("Enter number of mines (10-20): ")) #ask the user how many mines they want
            if 10 <= num_mines <= 20: #check if the number is inside the allowed range
                break #leave the loop when the input is valid
            print("Please enter a number between 10 and 20.") #tell the user the number is outside the allowed range
        except ValueError: #handle input that is not a number
            print("Please enter a valid number.") #tell the user to enter a valid number

    first_uncover = True #keep track of whether the first cell was uncovered
    game = None #game logic does not exist until mines are placed

    while True:  #keep the game running until win or loss
        display_board(board) #show the current board

        if game is not None: #check if game logic was created
            game_state = game.check_game_state() #get the current state from game logic
            print("Flags Remaining:", game.remaining_flags) #show remaining flags 
            print("Status:", game_state) #show current game status


            if game_state != "Playing": #check if the game is no longer playing
                break #leave the game loop

        print("\nEnter a column (A-J), row (1-10), and action.") #tell the user what values to enter

        print("Example: A 5 U") #show an example move

        print("U = uncover, F = flag") #explain the available actions

        user_input = input("Move: ").strip().upper().split() #get the move, remove extra spaces, make uppercase, and separate values

        if len(user_input) != 3: #check if the user entered exactly three values
            print("Invalid input. Example: A 5 U") #show the correct input format
            continue  #restart the loop
        
        col_input = user_input[0] #save the first value as the column
        row_input = user_input[1] #save the second value as the row
        action = user_input[2] #save the third value as the action
        
        if col_input not in "ABCDEFGHIJ" or len(col_input) != 1: #check if the column is between A and J
            print("Column must be A-J.") #tell the user the valid column range
            continue #restart the loop

        try: #try to convert the row into a number
            row = int(row_input) #convert the row input into an integer
            if row < 1 or row > 10: #check if the row is outside the board
                print("Row must be 1-10.") #tell the user the valid row range
                continue #restart the loop

        except ValueError: #handle a row that is not a number

            print("Row must be a number from 1-10.") #tell the user what type of value is needed
            continue #restart the loop

        if action not in ("U", "F"): #check if the action is uncover or flag
            print("Action must be U for uncover or F for flag.") #tell the user the valid actions
            continue #restart the loop

        row_index = row - 1 #change row 1-10 into index 0-9
        col_index = ord(col_input) - ord("A") #change column A-J into index 0-9

        if first_uncover and action == "U": #check if this is the first uncover
            board.place_mines(num_mines, row_index, col_index)#place mines while keeping the first cell safe
            game = GameLogic(board) #create the game logic using the board
            game.uncover_cell(row_index, col_index) #uncover the first selected cell
            first_uncover = False #mark that the first uncover already happened
            continue #restart the loop and show the updated board

        if first_uncover and action == "F": #check if the user tries to flag before the first uncover
            print("Please uncover a cell before placing flags.") #tell the user to uncover first
            continue #restart the loop

        if action == "U": #check if the action is uncover
            game.uncover_cell(row_index, col_index) #send the uncover action to game logic
        elif action == "F": #check if the action is flag
            game.toggle_flag(row_index, col_index) #send the flag action to game logic 

    display_board(board) #show the board one last time after the game ends

    print("\n" + game.check_game_state()) #print the final game state

if __name__ == "__main__":
    main()


