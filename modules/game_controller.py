# modules/game_controller.py

"""
Name: Elias
E-Mail: stipanel@hs-albsig.de
Erstelldatum: 24.05.2024
"""

import configparser
import time
from modules.universe import Universe

class GameController:
    """
    A class to control the simulation of the Game of Life.
    """

    def __init__(self, config_path='config.cfg'):
        """
        Initializes the GameController with the configuration file.

        Args:
            config_path (str): Path to the configuration file.
        """
        self.config = configparser.ConfigParser()
        self.config.read(config_path)

        game_config = self.config['GAME']
        visual_config = self.config['VISUAL']

        self.height = int(game_config['height'])
        self.width = int(game_config['width'])
        self.iterations = int(game_config['iterations'])
        self.ruleset = game_config['ruleset']
        self.init_alive_prob = float(game_config['init_alive_prob'])

        self.char_alive = visual_config['char_alive']
        self.char_dead = visual_config['char_dead']
        self.delay = float(visual_config['delay'])

        self.universe = Universe(self.height, self.width, self.ruleset)
        self.initialize_universe()

    def initialize_universe(self):
        """
        Initializes the universe with a random state based on the initial alive probability.
        """
        import random
        for row in range(self.height):
            for col in range(self.width):
                if random.random() < self.init_alive_prob:
                    self.universe.set_cell_state(row, col, 1)

    def run(self, steps=None):
        """
        Runs the simulation for a given number of steps.

        Args:
            steps (int): The number of steps to run the simulation.
        """
        steps = steps if steps is not None else self.iterations
        for _ in range(steps):
            self.display()
            self.universe.step()
            time.sleep(self.delay)

    def display(self):
        """
        Displays the current state of the universe.
        """
        for row in self.universe.grid:
            print(' '.join(self.char_alive if cell.is_alive() else self.char_dead for cell in row))
        print("\n")
