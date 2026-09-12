"""
Module Name: board_manager.py
Class Name: BoardManager

FIXME DELETE LATER: Kaitlyn & Lauren, please fill out the following:

Description: [Describe how this manages the 10x10 grid and mine placement]
Inputs: [Note any inputs, e.g., initial click coordinates]
Outputs: [Note what the class returns, like Cell objects]

Authors: 
Creation Date(s):
External Sources:
"""

"""
FIXME DELETE LATER

Remember to add in-code comments:
- comment major code blocks and/or individual lines to explain functionality
- indicate if code is origina, sourced, combined

"""

from cell import Cell

class BoardManager:
    """
    Tasks: Board Management (Kaitlyn) & Mine Placement (Lauren)
    """
    def __init__(self):
        # TODO (Kaitlyn): Initialize a 10x10 2D array of Cell objects.
        # TODO (Kaitlyn): Keep column (A-J) and row (1-10) labels in mind for setup.
        pass

    def get_cell(self, row: int, col: int) -> Cell:
        # TODO (Kaitlyn): Return the Cell object at the given coordinates.
        pass
    
    def get_neighbors(self, row: int, col: int) -> list:
        # TODO (Kaitlyn): Return a list of valid adjacent Cell objects.
        pass

    def place_mines(self, num_mines: int, first_row: int, first_col: int) -> None:
        # TODO (Lauren): Validate num_mines is between 10-20.
        # TODO (Lauren): Randomly place mines, ensuring (first_row, first_col) is mine-free.
        pass


"""
FIXME DELETE LATER

DO NOT CHANGE:
- FUNCTION DEFINITIONS OR RETURN TYPES

- Class and Method Names: BoardManager, get_cell, place_mines must remain the way they are written.
- Grid Size (Kaitlyn): must be exactly 10x10
- Mine Constraints (Lauren): Strictly enfource the rule that players can only specify between 10 and 20 mines
- First Click Safety (Lauren): place_mines must guarantee the first cell clicked is completely mine-free

WHAT CAN CHANGE:
- Implementation code: replace pass statements with logic 
- Label Mechanics (Kaitlyn): Decide most efficient way to manage required A-J and 1-10 labels

"""