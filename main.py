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
