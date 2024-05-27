# main.py

"""
Name: Elias
E-Mail: stipanel@hs-albsig.de
Erstelldatum: 26.05.2024
"""

from feature.game_controller import GameController

def main():
    # Initialize the game controller with the configuration file
    game_controller = GameController()
    
    # Run the simulation
    game_controller.run()

if __name__ == "__main__":
    main()

# Initialize the game controller with a 5x5 grid and standard rules
game_controller = GameController(5, 5, "23/3")

# Set some initial states
game_controller.universe.set_cell_state(1, 2, 1)
game_controller.universe.set_cell_state(2, 2, 1)
game_controller.universe.set_cell_state(3, 2, 1)

print("Initial State:")
game_controller.display()

# Run the simulation for 5 steps
game_controller.run(5)

print("\nState after 5 steps:")
game_controller.display()
