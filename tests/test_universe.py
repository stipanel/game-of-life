# tests/test_universe.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from modules.universe import Universe

def test_universe_initialization():
    universe = Universe(3, 3, "23/3")
    assert universe.get_cell_state(1, 1) == 0

def test_set_get_cell_state():
    universe = Universe(3, 3, "23/3")
    universe.set_cell_state(1, 1, 1)
    assert universe.get_cell_state(1, 1) == 1

def test_universe_step():
    universe = Universe(3, 3, "23/3")
    universe.set_cell_state(0, 1, 1)
    universe.set_cell_state(1, 1, 1)
    universe.set_cell_state(2, 1, 1)
    universe.step()
    assert universe.get_cell_state(1, 0) == 1
    assert universe.get_cell_state(1, 1) == 1
    assert universe.get_cell_state(1, 2) == 1
