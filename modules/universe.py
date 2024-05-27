# modules/universe.py

"""
Name: Elias
E-Mail: stipanel@hs-albsig.de
Erstelldatum: 13.05.2024
"""

from modules.cell import Cell
from modules.ruleset import Ruleset

class Universe:
    """
    A class to represent the universe in the Game of Life.

    Attributes:
        rows (int): The number of rows in the universe.
        cols (int): The number of columns in the universe.
        ruleset (Ruleset): The rules for the Game of Life.
        grid (List[List[Cell]]): The grid representing the cells of the universe.
    """

    def __init__(self, rows: int, cols: int, rules: str):
        """
        Initializes the Universe with the given dimensions and rules.

        Args:
            rows (int): The number of rows.
            cols (int): The number of columns.
            rules (str): The rules in the format "23/3".
        """
        self.rows = rows
        self.cols = cols
        self.ruleset = Ruleset(rules)
        self.grid = [[Cell(0) for _ in range(cols)] for _ in range(rows)]

    def get_cell_state(self, row: int, col: int) -> int:
        """
        Returns the state of the cell at the given position.

        Args:
            row (int): The row of the cell.
            col (int): The column of the cell.

        Returns:
            int: The state of the cell (0 or 1).
        """
        return self.grid[row][col].is_alive()

    def set_cell_state(self, row: int, col: int, state: int):
        """
        Sets the state of the cell at the given position.

        Args:
            row (int): The row of the cell.
            col (int): The column of the cell.
            state (int): The new state of the cell (0 or 1).
        """
        self.grid[row][col].set_state(state)

    def step(self):
        """
        Performs one step of the simulation and updates the state of the universe.
        """
        new_grid = [[Cell(0) for _ in range(self.cols)] for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                current_state = self.grid[row][col].is_alive()
                num_alive_neighbors = self._count_alive_neighbors(row, col)
                new_state = self.ruleset.calculate_next_state(current_state, num_alive_neighbors)
                new_grid[row][col].set_state(new_state)
        self.grid = new_grid

    def _count_alive_neighbors(self, row: int, col: int) -> int:
        """
        Counts the alive neighbors of a cell.

        Args:
            row (int): The row of the cell.
            col (int): The column of the cell.

        Returns:
            int: The number of alive neighbors.
        """
        neighbors = [
            (row-1, col-1), (row-1, col), (row-1, col+1),
            (row, col-1),                (row, col+1),
            (row+1, col-1), (row+1, col), (row+1, col+1)
        ]
        count = 0
        for r, c in neighbors:
            if 0 <= r < self.rows and 0 <= c < self.cols:
                count += self.grid[r][c].is_alive()
        return count
