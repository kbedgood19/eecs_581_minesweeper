"""
Module Name: cell_real.py
Class Name: Cell

Description: Represents one cell in the Minesweeper game board and stores its state, mine status, and number of adjacent mines.
Inputs: None
Outputs: Stores the cell's state, mine status, and adjacent mine count.

Author: Greeshma Kunduri
Creation Date: September 17, 2026
External Sources: ChatGPT was used to assist with understanding and implementing the Cell class based on the provided project requirements.

Basic Code Template/Outline: Marie Biernacki, Gemini
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
        # Initialize the following attributes to their default starting values:
        # self.state
        # self.is_mine
        # self.adjacent_mines
        self.state = 0
        self.is_mine = False
        self.adjacent_mines = 0



