# modules/ruleset.py

"""
Name: Elias
E-Mail: stipanel@hs-albsig.de
Erstelldatum: 13.05.2024
"""

class Ruleset:
    """
    A class to represent the rules for the Game of Life.

    Attributes:
        rules (str): A string representing the rules in the format "23/3".
    """

    def __init__(self, rules: str):
        """
        Initializes the Ruleset class with the given rules.

        Args:
            rules (str): The rules in the format "23/3".
        """
        self.rules = rules
        self.cell_survives, self.cell_born = self._parse_rules()

    def _parse_rules(self):
        """
        Parses the rules and extracts the survival and birth rules.

        Returns:
            tuple: Two lists containing the survival and birth rules.
        """
        survive, born = self.rules.split('/')
        return list(map(int, survive)), list(map(int, born))

    def calculate_next_state(self, current_state: int, num_alive_neighbors: int) -> int:
        """
        Calculates the next state of a cell based on the current rules.

        Args:
            current_state (int): The current state of the cell (0 or 1).
            num_alive_neighbors (int): The number of alive neighbors.

        Returns:
            int: The next state of the cell (0 or 1).
        """
        if current_state == 1:
            return 1 if num_alive_neighbors in self.cell_survives else 0
        else:
            return 1 if num_alive_neighbors in self.cell_born else 0
