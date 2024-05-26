# tests/test_ruleset.py

import pytest
from modules.ruleset import Ruleset

def test_ruleset_parsing():
    ruleset = Ruleset("23/3")
    assert ruleset.cell_survives == [2, 3]
    assert ruleset.cell_born == [3]

def test_calculate_next_state():
    ruleset = Ruleset("23/3")
    assert ruleset.calculate_next_state(1, 2) == 1
    assert ruleset.calculate_next_state(1, 1) == 0
    assert ruleset.calculate_next_state(0, 3) == 1
    assert ruleset.calculate_next_state(0, 2) == 0
