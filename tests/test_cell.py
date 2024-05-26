# tests/test_cell.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from modules.cell import Cell

def test_cell_initial_state():
    cell = Cell(1)
    assert cell.is_alive() == True

def test_cell_set_state():
    cell = Cell(0)
    assert cell.is_alive() == False
    cell.set_state(1)
    assert cell.is_alive() == True
