"""
Author: Denis Bajgora
Date:1/12/23
Course: TU857-2
Program Name: game.py

Program Description:

The main functionalities of this class include initializing the game state,
managing levels, and controlling the game flow through a level picker method.
This method sequentially activates each level, allowing the player to progress
through the game. After all levels are completed, the game state is set to
indicate the game's conclusion.
"""

from denis.Player import Player
from josh.level1 import Level1
from sean.level2 import Level2
from max.level3 import Level3
from denis.Levels import Level4
from cian.level5 import Level5
from jamie.level6 import Level6
import pygame


class Game:
    def __init__(self):
        self.game_run = True  # Flag to keep track of the game state
        self.next_level = 0  # Index for the next level to be played

        pygame.mixer.init()  # used for sound

        # Prompting the user to enter a name for the player
        self.player_name = input("Welcome Adventurer!, Enter a name please: ")

        # Creating a new Player instance with the entered name
        self.initialize_player(self.player_name) # initialize the player
        self.initialize_levels()  # Re-initialize all levels

    def initialize_player(self, player_name):
        self.player = Player(player_name)

    def initialize_levels(self):
        # Create new instances of each level
        level1 = Level1(self.player)
        level2 = Level2(self.player)
        level3 = Level3(self.player)
        level4 = Level4(self.player)
        level5 = Level5(self.player)
        level6 = Level6(self.player)

        # Storing the initialized levels in a list
        self.levels = [level1, level2, level3, level4, level5, level6]

    def level_picker(self):
        while self.game_run:
            # Looping through each level until all levels are completed
            while self.next_level < len(self.levels):
                # Starting the next level and then incrementing the level index
                self.levels[self.next_level].level_start() # Polymorphism
                self.next_level += 1

            # Asking the player if they want to replay the game
            print(f"Congrats {self.player_name}, you have beaten the game!")
            choice = input(
                "Would you like to replay the game? 'q' to quit, 'r' to "
                " replay: ")
            if choice == 'r'.lower():
                # Resetting the next_level to start from the beginning
                self.next_level = 0
                self.initialize_player(self.player_name)  # Re-initialize the
                # player
                self.initialize_levels()  # Re-initialize all levels
            if choice == 'q'.lower():
                print("Till another time, adventurer!\n")
                # Exiting the game
                self.game_run = False


# Creating an instance of the Game
game = Game()

# Checking if the game is running
if game.game_run:
    # If the game is running, start and progress through levels
    game.level_picker()
