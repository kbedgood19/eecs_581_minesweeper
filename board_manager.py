"""
Module Name: board_manager.py
Class Name: BoardManager

Description: board_manager.py manages the 10x10 grid. Creates and stores
            Cell objects, returns cells and their neighboring cells, 
            handles mine placements
Inputs: Row and column coordinates and mines
Outputs: Cell objects and their neighboring cells, updates board with mine
        locations 

Authors: Kaitlyn Bedgood, Lauren Lee
Creation Date(s): 9/12/2026
External Sources:https://www.geeksforgeeks.org/python/python-using-2d-arrays-lists-the-right-way/
                https://www.geeksforgeeks.org/python/multi-dimensional-lists-in-python/
                I used these two GeeksforGeeks articles to help traverse through 2D Lists
"""

import random # need for random mine placement
from cell_real import Cell #changed to match cell_real.py

class BoardManager:
    """
    Tasks: Board Management (Kaitlyn) & Mine Placement (Lauren)
    """
    def __init__(self):

        self.rows = 10
        self.cols = 10
        self.grid = [] #empty list that will hold rows of the board

        for row in range(self.rows): #loops ten times to create each row of board
            new_row = [] #empty list for cells in current row

            for col in range(self.cols): #loops 10 times to create col in current row
                new_row.append(Cell()) #create new cell object

            self.grid.append(new_row) #add row of cell objects to board

    def get_cell(self, row: int, col: int) -> Cell:
        
        return self.grid[row][col] #return cell object when given row and column
    
    def get_neighbors(self, row: int, col: int) -> list:
        
        neighbors = [] #empty list
        if row < 0 or row >= self.rows: #check if row is outside board
            return neighbors

        if col < 0 or col >= self.cols: #check if column is outside board
            return neighbors

        for row_offset in range(-1, 2): #check row above, current row, and row below
            for col_offset in range(-1, 2): #check col left, current col, and right col
                neighbor_row = row+ row_offset #find row position of neighbor
                neighbor_col = col + col_offset #find column position of neighbor

                if row_offset != 0 or col_offset != 0: #make sure original cell is not counted as it's neighbor
                    if neighbor_row >= 0 and neighbor_row < self.rows: #check neighbor row is in board
                        if neighbor_col >=0  and neighbor_col < self.cols: #check if neighbor col is in board
                            neighbors.append(self.grid[neighbor_row][neighbor_col]) #append valid neighbor cell to list

        return neighbors



    def place_mines(self, num_mines: int, first_row: int, first_col: int) -> None:
        # TODO (Lauren): Validate num_mines is between 10-20.
        # TODO (Lauren): Randomly place mines, ensuring (first_row, first_col) is mine-free.
          # (Lauren): Validate that the number of mines is between 10 and 20.
        if num_mines < 10 or num_mines > 20:
            raise ValueError("Number of mines must be between 10 and 20.")

        self.num_mines = num_mines
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
                self.grid[row][col].adjacent_mines = mine_count




