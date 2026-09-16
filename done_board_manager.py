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

import random # need for random mine placement
from cell_real import Cell #changed to match cell_real.py

class BoardManager:
    """
    Tasks: Board Management (Kaitlyn) & Mine Placement (Lauren)
    """
    def __init__(self):
        # (Kaitlyn): Initialize a 10x10 2D array of Cell objects.
        # (Kaitlyn): Keep column (A-J) and row (1-10) labels in mind for setup.
        self.rows = 10
        self.cols = 10
        self.grid = []

        for row in range(self.rows):
            new_row = []

            for col in range(self.cols):
                new_row.append(Cell())

            self.grid.append(new_row)

    def get_cell(self, row: int, col: int) -> Cell:
        # (Kaitlyn): Return the Cell object at the given coordinates.
        return self.grid[row][col]
    
    def get_neighbors(self, row: int, col: int) -> list:
        # (Kaitlyn): Return a list of valid adjacent Cell objects.
        neighbors = []
        if row < 0 or row >= self.rows:
            return neighbors

        if col < 0 or col >= self.cols:
            return neighbors

        for row_offset in range(-1, 2):
            for col_offset in range(-1, 2):
                neighbor_row = row+ row_offset
                neighbor_col = col + col_offset

                if row_offset != 0 or col_offset != 0:
                    if neighbor_row >= 0 and neighbor_row < self.rows:
                        if neighbor_col >=0  and neighbor_col < self.cols:
                            neighbors.append(self.grid[neighbor_row][neighbor_col])

        return neighbors

    def print_board(self):
        """
        print_board needs to finished once cell_real.py is finished
        need to print out the cell object and not just a "*"
        will need something like this
        for col in range(self.cols):
            print(" " + str(self.grid[row][col]) + " |", end="")
        
        """
        #label column
        print("    A   B   C   D   E   F   G   H   I   J")
        print("   +---+---+---+---+---+---+---+---+---+---+")

        #print each row of board
        for row in range(self.rows):
            print(str(row + 1).rjust(2) + " |", end="")

            for col in range(self.cols):
                print(" * |", end="")

            print()
            print("   +---+---+---+---+---+---+---+---+---+---+")


def place_mines(self, num_mines: int, first_row: int, first_col: int) -> None:
    # (Lauren): Validate that the number of mines is between 10 and 20.
    if num_mines < 10 or num_mines > 20:
        raise ValueError("Number of mines must be between 10 and 20.")

    # (Lauren): Create a list of all board coordinates that can contain mines.
    # The first clicked cell is excluded to guarantee first-click safety.
    available_cells = []

    for row in range(self.rows):
        for col in range(self.cols):
            if row != first_row or col != first_col:
                available_cells.append((row, col))

    # (Lauren): Randomly select locations for the mines.
    mine_locations = random.sample(available_cells, num_mines)

    # (Lauren): Place a mine in each randomly selected cell.
    for row, col in mine_locations:
        self.grid[row][col].is_mine = True

    # (Lauren): Calculate the number of mines surrounding every cell.
    for row in range(self.rows):
        for col in range(self.cols):
            # The mine itself does not need a neighbor mine count.
            # so if mine -> skip and continue to next cell
            if self.grid[row][col].is_mine:
                continue
            
            # Count the number of mines in neighboring cells.
            mine_count = 0

            # Check every neighboring cell.
            for neighbor in self.get_neighbors(row, col):
                # If the neighbor is a mine, increment the count.
                if neighbor.is_mine:
                    mine_count += 1

            # Set the neighbor mine count for the current cell.
            self.grid[row][col].neighbor_mines = mine_count


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
