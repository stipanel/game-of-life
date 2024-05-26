# modules/cell.py

"""
Name: Elias
E-Mail: stipanel@hs-albsig.de
Erstelldatum: 13.05.2024
"""

class Cell:
    def __init__(self, state: int):
        self.state = state

    def is_alive(self) -> bool:
        return self.state == 1

    def set_state(self, state: int):
        self.state = state