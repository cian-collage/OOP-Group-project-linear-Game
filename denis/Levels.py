"""
Author: Denis Bajgora
Date:1/12/23
Course: TU857-2
Program Name: Levels.py

Program Description:

The fourth level of a text-based adventure game is represented by the Level4
class in this programme. Players interact and make decisions in places like
Whispering Grove and Luminous Lake, which are located in a fantasy forest.
The course techniques for managing gameplay and introducing the
 level, enabling players to manage their stuff, find clues, and explore
 various regions.
"""


from abc import ABC, abstractmethod
import time
import pygame

from denis.Areas import LuminousLake
from denis.Areas import WhisperingGrove
from denis.Areas import CanopyWalkway
from denis.Areas import EchoingCaverns

class Level(ABC):
    def __init__(self, player):
        # Associate the level with a player object
        self.player = player

    @abstractmethod
    def introduction(self):
        # To be implemented in child classes, displays the level introduction
        pass

    @abstractmethod
    def level_start(self):
        # To be implemented in child classes, starts the level gameplay
        pass

class Level4(Level):
    def __init__(self, player):
        super().__init__(player)
        # Initialize locations specific to Level 4
        self.luminous_lake = LuminousLake(self.player)
        self.whispering_grove = WhisperingGrove(self.player)
        self.canopy_walkway = CanopyWalkway(self.player)
        self.echoing_caverns = EchoingCaverns(self.player)
        # List of locations in Level 4
        self.locations = [self.luminous_lake, self.whispering_grove,
                          self.canopy_walkway, self.echoing_caverns]
        self.current_pos = 0  # Player's current position
        self.game_flag = 0  # Flag to track game progress
        self.game_end_number = -1  # Flag value to end the game

    @staticmethod
    def play_main_sound():
        pygame.mixer.init()
        pygame.mixer.music.load("Mushroom Forest Theme.mp3")
        pygame.mixer.music.play(loops=10)

    def introduction(self):
        # Introduction narrative for Level 4
        print("Clutching the mysterious mushroom map, its intricate network" 
        " of paths and landmarks etched in bioluminescent ink, you navigate"
        " through the forest's depths.\n")
        print("You find yourself in a luminous glade, the air filled with "
              "spores that glimmer like tiny stars.\n")
        time.sleep(1)
        print("Gigantic mushrooms tower over you, their caps glowing softly"
              "in an array of colors.\n")
        time.sleep(1)
        print("The path behind you fades into the forest, hinting at the way "
              "back.\n")
        time.sleep(1)
        print("A gentle, misty breeze whispers through the trees, carrying "
              "distant, melodic sounds.\n")
        time.sleep(1)
        print("The path ahead winds deeper into the forest, where the "
              "mushrooms grow denser and the air is thick with mystery.\n")

    def level_start(self):
        # Starts Level 4 gameplay
        self.play_main_sound()
        self.introduction()

        while True:
            print("---Type anything to continue---\n")
            input()
            if self.game_flag == self.game_end_number:
                pygame.mixer.music.stop()
                break
            print("-------------------------------------------------------")
            # Display location choices
            for index, location in enumerate(self.locations):
                print(f"{index + 1}) Would you like to go to {location.name}\n")

            print(f"{(len(self.locations) + 1)}) to view your Inventory 👜\n")
            print(f"{(len(self.locations) + 2)}) to view your Clues 🧩\n")
            print("-------------------------------------------------------")

            while True:
                try:
                    choice = int(input("").lower())
                    if choice == (len(self.locations) + 1):
                        self.player.show_inventory()
                    elif choice == (len(self.locations) + 2):
                        self.player.show_main_clues()
                        self.player.show_level_clues()
                    break
                except Exception:
                    print("Invalid Input!")
            for index, location in enumerate(self.locations):
                if choice == (index + 1):
                    self.game_flag = location.location_scene()
