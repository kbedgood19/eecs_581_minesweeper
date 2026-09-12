"""
Module Name: main.py

FIXME DELETE LATER: Sabelli, please complete the following:

Description: [Describe how this handles the Command Line Interfae game loop and user input here]
Inputs: [Note expected user terminal inputs here]
Outputs: [Note expected outputs, like terminal grid rendering]

Author: 
Creation Date: 
External Sources:
"""

"""
FIXME DELETE LATER

Remember to add in-code comments:
- comment major code blocks and/or individual lines to explain functionality
- indicate if code is origina, sourced, combined

"""

from game_logic import GameLogic
from board_manager import BoardManager

def display_board(board: BoardManager) -> None:
    # TODO: Loop through the 10x10 board and print the current cell states.
    # TODO: Ensure columns (A-J) and rows (1-10) are clearly labeled.
    pass

def main():
    """
    Tasks: Main Function (Sabelli)
    """
    # TODO: Instantiate BoardManager and GameLogic.
    # TODO: Prompt user for the number of mines (10-20) to pass to place_mines().
    # TODO: Create a loop that runs while check_game_state() returns "Playing".
    # TODO: Inside the loop: display the board and get user input (row, col, uncover/flag).
    # TODO: Map valid inputs to game_logic.uncover_cell() or toggle_flag().
    # TODO: Once the loop ends, display the final board and the win/loss message.
    pass

if __name__ == "__main__":
    main()


"""
FIXME DELETE LATER

DO NOT CHANGE:
- FUNCTION DEFINITIONS OR RETURN TYPES

- Terminal-Based Input/Output: no longer using Tkinter due to time constraints, only use print() and input() for Command Line Interface
- Game States: Must rely exactly on the "Playing", "Game Over: Loss", and "Victory" strings returned by check_game_state
- Mine Constraints: must explicitly prompt the user for the mine count and enforce the 10 to 20 limit before the first click

WHAT CAN CHANGE:
- Input Validation: free to design how to validate user terminal inputs (such as using try/except blocks to handle typos)
- Visual Design: creative freedom regarding how the Command Line Interface board is rendered, as long as it features required A-J and 1-10 labels
- Helper Functions: can add other input-parsing helper methods if it makes the main() function cleaner

"""