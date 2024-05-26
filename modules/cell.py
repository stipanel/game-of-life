# modules/cell.py

"""
Name: Elias
E-Mail: stipanel@hs-albsig.de
Erstelldatum: 13.05.2024
"""

class Cell:
    """
    A class to represent a cell in the Game of Life.

    Attributes:
        state (int): The state of the cell (0 or 1).
    """

    def __init__(self, state: int):
        """
        Initializes the Cell class with the given state.

        Args:
            state (int): The state of the cell (0 or 1).
        """
        self.state = state

    def is_alive(self) -> bool:
        """
        Returns whether the cell is alive.

        Returns:
            bool: True if the cell is alive, False otherwise.
        """
        return self.state == 1

    def set_state(self, state: int):
        """
        Sets the state of the cell.

        Args:
            state (int): The new state of the cell (0 or 1).
        """
        self.state = state
