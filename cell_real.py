"""
Module Name: cell.py
Class Name: Cell

FIXME DELETE LATER: Greeshma, please fill in the following:

Description: Represents one cell in the Minesweeper game board and stores its state, mine status, and number of adjacent mines.
Inputs: None
Outputs: Stores the cell's state, mine status, and adjacent mine count.

Author: Greeshma Kunduri
Creation Date: September 17, 2026
External Sources:
"""


"""
FIXME DELETE LATER

Remember to add in-code comments:
- comment major code blocks and/or individual lines to explain functionality
- indicate if code is origina, sourced, combined

"""

class Cell:
    """
    Task: Cell Object (Greeshma)
    
    Attributes:
    - state (int): 0=covered, 1=flagged, 2=uncovered number, 3=mine
    - is_mine (bool): True if mine, False otherwise
    - adjacent_mines (int): Number of adjacent mines (0-8)
    """
    def __init__(self):
        # TODO: Initialize the following attributes to their default starting values:
        # self.state
        # self.is_mine
        # self.adjacent_mines
        self.state = 0
        self.is_mine = False
        self.adjacent_mines = 0


"""
FIXME DELETE LATER

DO NOT CHANGE:
- FUNCTION DEFINITIONS OR RETURN TYPES

- Class Name: must remain "Cell"
- Attribute Names: state, is_mine, and adjacent_mines
- Attribute Types: state must remain an integer mapped to 0-3, is_mine must remain a boolean, adjacent_mines must be an integer

WHAT CAN CHANGE:
- Implementation code: replace pass statement with logic setting up the default states

"""
