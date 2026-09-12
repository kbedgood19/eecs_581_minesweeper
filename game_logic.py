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
        # TODO (Ximena): Initialize game state variables (e.g., current state).
        pass

    def uncover_cell(self, row: int, col: int) -> None:
        # TODO (Jaydine): Uncover cell. If adjacent_mines == 0, call recursive_reveal.
        pass

    def recursive_reveal(self, row: int, col: int) -> None:
        # TODO (Jaydine): Recursively uncover adjacent cells using the board's neighbor lookup.
        # use the get_neighbors 
        pass

    def toggle_flag(self, row: int, col: int) -> None:
        # TODO (Ximena): Toggle flag state on the cell and update total remaining flags.
        # TODO (Ximena): Prevent uncovering if a cell is flagged.
        pass

    def check_game_state(self) -> str:
        # TODO (Ximena): Return exactly "Playing", "Game Over: Loss", or "Victory".
        pass

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