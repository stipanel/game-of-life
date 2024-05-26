# modules/game_controller.py

"""
Name: Elias
E-Mail: stipanel@hs-albsig.de
Erstelldatum: 24.05.2024
"""

from modules.universe import Universe

class GameController:
    """
    A class to control the simulation of the Game of Life.

    Attributes:
        universe (Universe): The universe where the simulation takes place.
    """

    def __init__(self, rows: int, cols: int, rules: str):
        """
        Initializes the GameController with the given dimensions and rules.

        Args:
            rows (int): The number of rows.
            cols (int): The number of columns.
            rules (str): The rules in the format "23/3".
        """
        self.universe = Universe(rows, cols, rules)

    def run(self, steps: int):
        """
        Runs the simulation for a given number of steps.

        Args:
            steps (int): The number of steps to run the simulation.
        """
        for _ in range(steps):
            self.universe.step()

    def display(self):
        """
        Displays the current state of the universe.
        """
        for row in self.universe.grid:
            print(' '.join(str(cell.is_alive()) for cell in row))
