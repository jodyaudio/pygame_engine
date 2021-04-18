from setup import *
import constants as c


def main():
    """Main function. The program starts here :)
    Most of the below functions are all imported through the setup module above."""
    initialize_game()                                                               # Initialize the game
    display = get_display()                                                         # Get display
    clock = get_clock()                                                             # Get clock
    game_states = get_game_states()                                                 # Get all game states
    controller = get_controller(display, clock, game_states, c.STARTING_STATE)      # Load game controller
    controller.run()                                                                # Run this bad boy!


# If Guard
if __name__ == '__main__':
    main()
