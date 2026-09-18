"""
Module Name: game_logic.py
Class Name: GameLogic

Description: This manages the game logic, such as uncovering cells, recursively revealing cells with no adjacent mines, toggling flags, tracking remaining flags, and checking status of the game.
Inputs: board_manager. uncover_cell() and toggle_flag() take a row and column to identify the selected cell.
Outputs: uncover_cell() and toggle_flag() update the state of the selected cells. check_game_state() returns "Playing", "Game Over: Loss", or "Victory".

Authors: Ximena Bustos, Jaydine Stiles
Creation Date(s): 09/14/26
External Sources: https://www.askpython.com/python/examples/create-minesweeper-using-python I used this to get an idea of how the code will work.
"""

from board_manager import BoardManager

class GameLogic:
    """
    Tasks: Reveal Logic (Jaydine) & Flags + Win/Loss (Ximena)
    """
    def __init__(self, board: BoardManager):
        self.board = board
        self.remaining_flags = board.num_mines
        self.game_state = "Playing"

    def uncover_cell(self, row: int, col: int) -> None:
        #uncover the selected cell
        #ignore coordinates outside the board
        if row < 0 or row >= self.board.rows or col < 0 or col >= self.board.cols:
            return

        cell = self.board.get_cell(row, col)

        #don't uncover flagged or already uncovered cells
        if cell.state == 1 or cell.state == 2 or cell.state == 3:
            return

        #reveal the mine if the selected cell is a mine
        if cell.is_mine:
            cell.state = 3
            return

        #recursively reveal neighbors if there are no adjacent mines
        if cell.adjacent_mines == 0:
            self.recursive_reveal(row, col)
        else:
            cell.state = 2

    def recursive_reveal(self, row: int, col: int) -> None:
        #ignore coordinates outside the board
        if row < 0 or row >= self.board.rows or col < 0 or col >= self.board.cols:
            return

        cell = self.board.get_cell(row, col)

        #don't reveal flagged cells, mines, or already uncovered cells
        if cell.state != 0 or cell.is_mine:
            return

        cell.state = 2 #uncover the cell

        #stop if the cell has an adjacent mine
        if cell.adjacent_mines != 0:
            return

        neighbors = self.board.get_neighbors(row, col) #get neighboring cells

        #check each surrounding position
        for neighbor_row in range(max(0, row - 1), min(self.board.rows, row + 2)):
            for neighbor_col in range(max(0, col - 1), min(self.board.cols, col + 2)):
                neighbor = self.board.get_cell(neighbor_row, neighbor_col)

                #reveal the neighbor if it is in the neighbor list
                if neighbor in neighbors:
                    self.recursive_reveal(neighbor_row, neighbor_col)

    def toggle_flag(self, row: int, col: int) -> None:
        # Checks if the row and column are inside of the board.
        # Ignores coordinates ouside of the board.
        if row < 0 or row >= self.board.rows or col < 0 or col >= self.board.cols:
            return
        
        # Gets the cell object at the selected row and column.
        cell = self.board.get_cell(row, col)

        # This doesn't allow revealed cells to be flagged.
        # 2 = revealed safe cell and 3 = revealed mine.
        if cell.state == 2 or cell.state == 3:
            return
        
        # Removes an existing flag, it already flagged.
        # 1 = cell currently has a flag.
        if cell.state == 1:
            cell.state = 0
            self.remaining_flags += 1       # Removing the flag gives the player one more flag.

        # If the cell is hiiden and there are flags available, places a flag on the cell.
        # 0 = cell is currently hidden.
        elif cell.state == 0 and self.remaining_flags > 0:
            cell.state = 1
            self.remaining_flags -= 1       # Placed flag means using the player's available flags.
        

    def check_game_state(self) -> str:
        # Goes through every cell on the board to check if the player 
        # has revealed a mine.
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                cell = self.board.get_cell(row, col)

                # 3 = mine had been revealed.
                # Played has lost the game.
                if cell.state == 3:
                    self.game_state = "Game Over: Loss"
                    return self.game_state
                
        # If no mine has been revealed, checks whether the player
        # has revealed every cell that is not a mine.
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                cell = self.board.get_cell(row, col)

                # If the cell is not a mine and it hasn't been revealed,
                # there are more safe cells to be uncovered.
                if not cell.is_mine and cell.state != 2:
                    self.game_state = "Playing"
                    return self.game_state
                
        # All safe cells have been revealed.
        # The player has won.
        self.game_state = "Victory"
        return self.game_state