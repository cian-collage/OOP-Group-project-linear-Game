"""
Author: Denis Bajgora
Date:1/12/23
Course: TU857-2
Program Name: Player.py

Program Description:

The 'Player' class in this game represents the user's character, equipped with
features for inventory management and clue collection. It initializes with a
player's name and a starting coin count. The class allows players to add or
remove items from their inventory and collect two types of clues: main clues
and level-specific clues. Additionally, it includes methods to display the
contents of the player's inventory and the clues collected. This class is
essential for managing the player's progress and interactions within the game.
"""


class Player:
    # Constructor method to initialize a new player with a name
    def __init__(self, name):
        # Player's name
        self.name = name
        # List to store player's items
        self.inventory = []
        # List to store main clues collected by the player
        self.main_clues = []
        # List to store level-specific clues
        self.level_clues = []
        # Initialize player's coin count
        self.coins = 10
        # Greeting message to the player
        print(f"Welcome {name}!\n")

    # Method to display all items in the player's inventory
    def show_inventory(self):
        print("The items in your inventory are:\n")
        for item in self.inventory:
            print(item + '\n')

    # Method to display all main clues collected by the player
    def show_main_clues(self):
        print("Main Clues are:\n")
        for main_clue in self.main_clues:
            print(main_clue + '\n')

    # Method to display all level-specific clues collected by the player
    def show_level_clues(self):
        print("Level Clues are:\t")
        for level_clue in self.level_clues:
            print(level_clue + '\n')

    # Method to add an item to the player's inventory
    def add_item(self, item):
        print("New item - ", item)
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    # Method to add a main clue to the player's collection
    def add_main_clue(self, main_clue):
        self.main_clues.append(main_clue)

    # Method to add a level-specific clue to the player's collection
    def add_level_clue(self, level_clue):
        self.level_clues.append(level_clue)
