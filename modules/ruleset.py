# modules/ruleset.py

"""
Name: Elias
E-Mail: stipanel@hs-albsig.de
Erstelldatum: 13.05.2024
"""

class Ruleset:
    def __init__(self, rules: str):
        self.rules = rules
        self.cell_survives, self.cell_born = self._parse_rules(rules)

    def _parse_rules(self) -> (list[int], list[int]):
        survive, born = self.rules.split('/')
        return list(map(int, survive)), list(map(int, born))

    def calculate_next_state(self, current_state: int, num_alive_neighbors: int) -> int:
        if current_state == 1:
            return 1 if num_alive_neighbors in self.cell_survives else 0
        else:
            return 1 if num_alive_neighbors in self.cell_born else 0
