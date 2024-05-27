# tests/test_game_controller.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from feature.game_controller import GameController

def test_game_controller_initialization():
    controller = GameController(3, 3, "23/3")
    assert controller.universe.get_cell_state(1, 1) == 0

def test_game_controller_run():
    controller = GameController(3, 3, "23/3")
    controller.universe.set_cell_state(0, 1, 1)
    controller.universe.set_cell_state(1, 1, 1)
    controller.universe.set_cell_state(2, 1, 1)
    controller.run(1)
    assert controller.universe.get_cell_state(1, 0) == 1
    assert controller.universe.get_cell_state(1, 1) == 1
    assert controller.universe.get_cell_state(1, 2) == 1
