"""
Module Name: game_logic.py
Class Name: GameLogic

FIXME DELETE LATER: Jaydine & Ximena, please fill out the following

Description: [Describe how this manages uncover logic, flagging, and game state here]
Inputs: [Note expected inputs, e.g., the board manager instance]
Outputs: [Note expected outputs, e.g., game state strings]

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

from board_manager import BoardManager

class GameLogic:
    """
    Tasks: Reveal Logic (Jaydine) & Flags + Win/Loss (Ximena)
    """
    def __init__(self, board: BoardManager):
        self.board = board
        # TODO (Ximena): Initialize remaining flags based on total mines (10-20).
        self.remaining_flags = board.num_mines
        # TODO (Ximena): Initialize game state variables (e.g., current state).
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
        # TODO (Ximena): Toggle flag state on the cell and update total remaining flags.
        # TODO (Ximena): Prevent uncovering if a cell is flagged.
        # Ignores coordinates ouside of the board.
        if row < 0 or row >= self.board.rows or col < 0 or col >= self.board.cols:
            return
        
        cell = self.board.get_cell(row, col)
        # This doesn't allow revealed cells to be flagged.
        if cell.state == 2 or cell.state == 3:
            return
        
        # Removes an existing flag.
        if cell.state == 1:
            cell.state = 0
            self.remaining_flags += 1

        # Adds flag if flags are available.
        elif cell.state == 0 and self.remaining_flags > 0:
            cell.state = 1
            self.remaining_flags -= 1
        

    def check_game_state(self) -> str:
        # TODO (Ximena): Return exactly "Playing", "Game Over: Loss", or "Victory".
        # Checks for a revealed mine.
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                cell = self.board.get_cell(row, col)

                if cell.state == 3:
                    self.game_state = "Game Over: Loss"
                    return self.game_state
                
        # Checks whether every safe cell has been revealed
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                cell = self.board.get_cell(row, col)

                if not cell.is_mine and cell.state != 2:
                    self.game_state = "Playing"
                    return self.game_state
                
        # All safe cells have been revealed.
        self.game_state = "Victory"
        return self.game_state
        

"""
FIXME DELETE LATER

DO NOT CHANGE:
- FUNCTION DEFINITIONS OR RETURN TYPES

- Class and Method Names: GameLogic, uncover_cell, toggle_flag, check_game_state must remain exactly the same
- State Returns (Ximena): check_game_state must return exact status indicators ("Playing", "Game Over: Loss", and "Victory")
- Recursive Reveal (Jaydine): recursive logic must be used to uncover adjacent cell
- Flag Rules (Ximena): must enforce that flagged cells cannot be uncovered until they are manually unflagged

WHAT CAN CHANGE:
- Implementation code: replace pass statements with logic 
- Win/Loss Helpers (Ximena): can add private helper methods if it makes calculating victory condition (all non-mine cells uncovered) easier

"""