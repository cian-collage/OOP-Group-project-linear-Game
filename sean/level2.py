"""
Program Name: level2.py

Author: Sen O'Connor

Program Description:

This is the 2nd level in our six-level game, focusing on the player's journey to infiltrate a city.
The level includes dialogues, choices, and potential deals with the barbarians, impacting the storyline.
Key elements include a barbarian camp and a dark alley with a secret meeting and a colored slab puzzle.
Completing the puzzle unlocks crucial items for progressing in the game.
The player has the option to strike deals, face consequences, and explore alternative paths.
The program includes classes and methods for managing player actions, interactions, and puzzles.

Date: 03/12/2023
"""

# Local Module Imports
from cian.characters import NPC
from sean.locationClass import Location
from denis.Player import Player
from sean.fight import fight, User, RedCloakEnemy
from sean.dice_game import roll_dice
from sean.colour_puzzle import ColoredSlabPuzzle

# Standard Library Imports
import time
import pygame


class Level2(Location):
    def __init__(self, player):

        # Initialize the Level2 instance by calling the superclass constructor
        super().__init__("City",
                         ["Outside City Walls", "Barbarian Group",
                          "Dark Alley", "Back City Walls",
                          "Around City Walls", "City Streets"],
                         ["City Guard", "Barbarian", "Red Cloak Man"],
                         [])

        # Set initial state and store player instance
        self.current_location = self.sublocation[0]
        self.player = player

        # Initialize NPC instances
        self.city_guard = NPC("City Guard",
                              ["Halt! What business do "
                               "you have here stranger?",
                               "Kidnapping you say? Haven't "
                               "heard anything about that. Although I did "
                               "oversee some sketchy figures talking nearby",
                               "You already asked me about the "
                               "kidnappings",
                               "Ah, I see you have a city pass",
                               "You may proceed stranger",
                               "Hold! You can't enter without a "
                               "city pass",
                               "Safe travels, stranger"
                               ],
                              "City guard saw some shady characters talking "
                              "near the "
                              "city gates.",
                              "",
                              "")
        self.barbarian = NPC("Barbarian Leader",
                             ["Looky here boys! Some fresh meat",
                              "I am in need of something as well. Perhaps we "
                              "can strike a deal..",
                              "You retrieve my prized dagger and I offer you "
                              "our services. What say you?",
                              "Wonderful. My dagger was stolen by a man in a "
                              "red cloak.\n"
                              "I think I saw him head around the back of the "
                              "city",
                              "Off ya hop now fresh meat and don't come back "
                              "without my dagger!",
                              "Stop wasting my time then! Scram!",
                              "You have returned. With my prized dagger I "
                              "hope?",
                              "Hold on now, I also want some gold from you. "
                              "You look as though you have a bit to spare",
                              "I don't remember no deal. Do you boys?",
                              "That's what I like to hear, get 'em boys!",
                              "Suit yourself. Thanks for the dagger",
                              "Return with the dagger or not at all!",
                              "Want to take me up on my offer now?",
                              "See that wasn't so hard. My dagger was stolen "
                              "by a man in a red cloak.\n I think I saw him "
                              "head around the back of the city",
                              "Off ya hop now fresh meat and don't come "
                              "back without my dagger!",
                              "Why do you keep approaching me then?!"],
                             "The barbarian's prized dagger was stolen by a "
                             "man in a red cloak",
                             "",
                             "")
        self.red_cloak_man = NPC("Red Cloaked Figure",
                                 ["What do we have here?",
                                  "You'll have to win it fair and square",
                                  "I'll play you in a game of dice for it",
                                  "Back off stranger! This is mine! I found "
                                  "it!",
                                  "I told you to back off! My precious!",
                                  "You'll have to win it off me in dice then\n"
                                  "and i never lose in dice!",
                                  "So this is how it'll be"],
                                 "",
                                 "Prized Dagger",
                                 "")

        # Boolean variables to track game progress and prevent double interactions
        self.__guard_interacted = False
        self.__guard_asked = False
        self.__barbarians_asked = False
        self.__deal_made = False
        self.__deal_complete = False
        self.__cloak_figure_interact = False
        self.__cloak_figure_fin = False
        self.__dark_alley_investigated = False
        self.puzzle_complete = False

        pygame.mixer.init()  # used for sound

    def level_start(self):

        # Start the level by initiating actions outside the city
        self.outside_city()

    @staticmethod
    def fight_song():
        pygame.mixer.music.load("Level 2 Fight Song.mp3")
        pygame.mixer.music.play(loops=-1)

    @staticmethod
    def wandering_song():
        pygame.mixer.music.load("KaerMorhen.mp3")
        pygame.mixer.music.play(loops=-1)

    @staticmethod
    def music_stop():
        pygame.mixer.music.stop()

    def outside_city(self):
        self.current_location = self.sublocation[0]

        # Display initial scene outside the city gates
        print(f"{self.current_location} - "
              f"The coldness of the night creeps into your soul.\n"
              f"You see the silhouette of the towering city gates ahead of "
              f"you, guarded by vigilant city guards.")

        # Function to pause code run-through
        time.sleep(2)

        self.wandering_song()

        while True:
            action = input("\nWhat will you do?\n"
                           "1) Approach the city gates\n"
                           "2) Explore Around the City Walls\n"
                           "3) Check the immediate area\n")

            if action == "1":
                self.guard_interaction()
            elif action == "2":
                self.explore_surroundings()
            elif action == "3":
                print("\nYou look around to see if there is a way to get into "
                      "the city.\n")
                time.sleep(1)
                self.barbarian_camp()

            if self.current_location == self.sublocation[5]:
                # Player enters the city, display the city scene and exit the loop
                print(f"You have entered the city! You are now in the "
                      f"{self.current_location}.")
                time.sleep(1)
                print("The hustle and bustle of the city's inhabitants "
                      "surrounds you.")
                time.sleep(2)
                self.summary()
                break  # Exit the loop once the player enters the city

    def guard_interaction(self):

        # Display initial dialogue from the city guard
        print(self.city_guard.say_dialogue(self.city_guard.dialogue[0]), "\n")

        while not self.__guard_interacted:
            interaction = int(input("1) Ask about the kidnapping\n"
                                    "2) Ask if you can get by\n"
                                    "3) Leave the city gates\n"))

            if interaction == 1:

                # Player asks about the kidnapping
                if not self.__guard_asked:
                    # If it's the first time, display specific dialogue and add a clue to the player's inventory
                    print(self.city_guard.say_dialogue
                          (self.city_guard.dialogue[1]), "\n")
                    time.sleep(1)
                    self.add_clue(self.city_guard.clue())
                    self.review_clues()
                    print("")
                    self.__guard_asked = True
                else:
                    # If already asked, display a different response
                    print(self.city_guard.say_dialogue
                          (self.city_guard.dialogue[2]), "\n")
                    time.sleep(1)
            elif interaction == 2:
                # If the player has a city pass, display corresponding dialogue and allow entry into the city
                if "City Pass" in self.player.inventory:
                    print(self.city_guard.say_dialogue
                          (self.city_guard.dialogue[3]), "\n")
                    time.sleep(1)
                    print(self.city_guard.say_dialogue
                          (self.city_guard.dialogue[4]), "\n")
                    time.sleep(1)
                    self.current_location = self.sublocation[5]
                    self.__guard_interacted = True
                else:
                    print(self.city_guard.say_dialogue
                          (self.city_guard.dialogue[5]), "\n")
                    time.sleep(1)
            elif interaction == 3:
                print(self.city_guard.say_dialogue
                      (self.city_guard.dialogue[6]))
                time.sleep(1)
                break  # Exit the loop, indicating the end of guard interaction

    def explore_surroundings(self):
        # Set the current location to the back of the city walls
        self.current_location = self.sublocation[3]
        print("\nYou notice a dark alley at the back of the city walls\n")
        time.sleep(2)
        exploration_result = input("1) Investigate the dark alley\n"
                                   "2) Examine the back of the city "
                                   "walls\n"
                                   "3) Return to the city gates\n")

        if exploration_result == "1":
            # Player chooses to investigate the dark alley
            self.current_location = self.sublocation[2]
            self.dark_alley()  # Run method for the dark alley interaction

        elif exploration_result == "2":
            # Player examines the back of the city walls
            if not self.__cloak_figure_fin:
                self.visited("Back City Walls")
                print("\nYou examine the back of the city walls.\n")
                time.sleep(1)
                if self.__deal_made and not self.__cloak_figure_interact:
                    # If deal with barbarians made and have not interacted with red cloaked man
                    print("You see a figure hiding at the back of the city "
                          "walls.\n"
                          "They are dressed in a red cloak and look to be "
                          "trying to hide something")
                    time.sleep(2)
                    print("\nYou notice that this is the man the barbarian "
                          "was talking about.")
                    time.sleep(1)
                    print("\nYou see the prized dagger in his hand")
                    time.sleep(1)
                    print(self.red_cloak_man.say_dialogue
                          (self.red_cloak_man.dialogue[0]), "\n")
                    time.sleep(1)
                    print(f"{self.player.name}:\n I'll be needing that dagger\n")
                    time.sleep(1)
                    print(self.red_cloak_man.say_dialogue
                          (self.red_cloak_man.dialogue[1]), "\n")
                    time.sleep(1)
                    if 'Chaos Sword' in self.player.inventory:
                        # If Chaos Sword in inventory, Player chooses to fight or play a dice game with the cloaked
                        # figure
                        print(self.red_cloak_man.say_dialogue
                              (self.red_cloak_man.dialogue[2]), "\n")
                        cloaked_figure_option = input("Do you want to fight "
                                                      "him for it or play "
                                                      "his little game?\n"
                                                      "1) Fight him!\n"
                                                      "2) Game time!\n")
                        if cloaked_figure_option == "1":
                            print(f"{self.player.name}:\n Give it to me\n")
                            time.sleep(1)
                            self.music_stop()
                            self.fight_song()
                            user = User(self.player.name)
                            red_cloak = RedCloakEnemy()
                            prize = fight(user, red_cloak)
                            if prize:
                                # Player wins and adds an item to inventory
                                self.player.add_item(prize)
                                self.player.show_inventory()
                                print("You gained 25 coins from "
                                      "beating him.")
                                self.player.coins += 25
                            self.__cloak_figure_fin = True
                            self.music_stop()  # stops current music
                            self.wandering_song()
                        elif cloaked_figure_option == "2":
                            print(f"{self.player.name}:\n Let's play then\n")
                            time.sleep(1)
                            self.music_stop()
                            self.fight_song()
                            prize = roll_dice()
                            if prize:
                                # Player wins and adds an item to inventory
                                self.player.add_item(prize)
                                self.player.show_inventory()
                                print("You gained 25 coins from "
                                      "beating him.")
                                self.player.coins += 25
                            self.__cloak_figure_fin = True
                            self.music_stop()
                            self.wandering_song()
                    else:
                        # Player doesn't have the Chaos Sword, plays the dice game
                        print(self.red_cloak_man.say_dialogue
                              (self.red_cloak_man.dialogue[2]), "\n")
                        time.sleep(1)
                        print(f"{self.player.name}:\n Let's play then\n")
                        time.sleep(1)
                        self.music_stop()
                        self.fight_song()
                        prize = roll_dice()
                        if prize:
                            # Player wins and adds an item to inventory
                            self.player.add_item(prize)
                            self.player.show_inventory()
                            print("You gained 25 coins from "
                                  "beating him.")
                            self.player.coins += 25
                        self.__cloak_figure_fin = True
                        self.music_stop()
                        self.wandering_song()

                elif not self.__deal_made and not self.__cloak_figure_interact:
                    # If player has not made the deal and has not seen the red cloaked man before
                    print("You see a figure hiding at the back of the city "
                          "walls.\n"
                          "They are dressed in a red cloak and look to be "
                          "trying to hide something.\n")
                    time.sleep(2)
                    print("You approach the man to ask if there is a way in.")
                    time.sleep(1)
                    print(self.red_cloak_man.say_dialogue
                          (self.red_cloak_man.dialogue[0]), "\n")
                    time.sleep(1)
                    print("He seems deep in admiration to what he is holding "
                          "but notices you when you get closer.")
                    time.sleep(2)
                    print(self.red_cloak_man.say_dialogue
                          (self.red_cloak_man.dialogue[3]), "\n")
                    time.sleep(1)
                    print("You back off slowly. You don't want to get into "
                          "any unnecessary trouble.")
                    time.sleep(1)
                    self.__cloak_figure_interact = True

                elif self.__deal_made and self.__cloak_figure_interact:
                    # Player comes back to the cloaked figure after making a deal
                    print("You come back to the cloaked man.")
                    time.sleep(1)
                    print(self.red_cloak_man.say_dialogue
                          (self.red_cloak_man.dialogue[4]), "\n")
                    time.sleep(1)
                    print("You notice now that this is the man the barbarian "
                          "was talking about.")
                    time.sleep(1)
                    print("You see the prized dagger in his hand.")
                    time.sleep(1)
                    print(f"{self.player.name}:\n I'll be needing that dagger.\n")
                    time.sleep(1)
                    print(self.red_cloak_man.say_dialogue
                          (self.red_cloak_man.dialogue[5]), "\n")
                    time.sleep(1)
                    if 'Chaos Sword' in self.player.inventory:
                        # Player chooses to fight or play a die game with the cloaked figure
                        cloaked_figure_option = input("Play his little dice "
                                                      "game or rip it from "
                                                      "his cold dead hands?\n"
                                                      "1) Fight him!\n"
                                                      "2) Game time!\n")
                        # Player makes a choice between fighting or playing a game
                        if cloaked_figure_option == "1":
                            # Player chooses to fight
                            print(f"{self.player.name}:\n I'll be taking that "
                                  f"dagger.\n")
                            time.sleep(1)
                            self.music_stop()
                            self.fight_song()
                            print(self.red_cloak_man.say_dialogue
                                  (self.red_cloak_man.dialogue[6]), "\n")
                            time.sleep(1)
                            user = User(self.player.name)
                            red_cloak = RedCloakEnemy()
                            prize = fight(user, red_cloak)
                            if prize:
                                # Player wins and gains the prize
                                self.player.add_item(prize)
                                self.player.show_inventory()
                                print("You gained 25 coins from "
                                      "beating him.")
                                self.player.coins += 25
                            self.__cloak_figure_fin = True
                            self.music_stop()
                            self.wandering_song()
                        elif cloaked_figure_option == "2":
                            # Player chooses the dice game
                            print(f"{self.player.name}:\n Let's play then.\n")
                            time.sleep(1)
                            self.music_stop()
                            self.fight_song()
                            prize = roll_dice()
                            if prize:
                                # Player wins and adds item to inventory

                                self.player.add_item(prize)
                                self.player.show_inventory()
                                print("You gained 25 coins from "
                                      "beating him.")
                                self.player.coins += 25
                            self.__cloak_figure_fin = True
                            self.music_stop()
                            self.wandering_song()
                    else:
                        # If player doesn't have sword in inventory
                        print(f"{self.player.name}:\n Let's play then.\n")
                        time.sleep(1)
                        self.fight_song()
                        prize = roll_dice()
                        if prize:
                            # Player wins and adds item to inventory
                            self.player.add_item(prize)
                            self.player.show_inventory()
                            print("You gained 25 coins from "
                                  "beating him.")
                            self.player.coins += 25
                        self.__cloak_figure_fin = True
                        self.music_stop()
                        self.wandering_song()
                else:
                    print("You dont want to cause any trouble so you stay "
                          "away from the cloaked figure.\n")
                    time.sleep(2)
            else:
                print("You lost and can't get the prized dagger now.\n"
                      "You'll have to find another way into the city\n")
                time.sleep(2)

        elif exploration_result == "3":
            print("You decide to return to the city gates.\n")
            time.sleep(1)

        else:
            print("Invalid option.\n")

    def barbarian_camp(self):
        # Set the current location to the Barbarian Group sublocation
        self.current_location = self.sublocation[1]

        # If the Barbarian Group has not been visited, mark it as visited
        if "Barbarian Group" not in self.visited_sublocations:
            self.visited("Barbarian Group")

        # If the player hasn't interacted with the barbarians yet
        if not self.__barbarians_asked:
            # Player chooses an option related to the barbarian camp
            barbarian_option = input("1) Look for a distraction\n"
                                     "2) Return to the previous options\n")

            if barbarian_option == "1":
                # Player looks for a distraction
                print("While scanning the surroundings, you notice a group of barbarians nearby.\n")
                time.sleep(2)
                print("The barbarians seem rowdy but open to negotiation.\n")
                time.sleep(1)
                # Player decides whether to approach the barbarians
                approach_barbarians = input("Do you want to approach them?\n"
                                            "1) Yes, approach the barbarians\n"
                                            "2) No, return to the previous options\n")

                if approach_barbarians == "1":
                    # Player approaches the barbarians
                    print("You approach the barbarians cautiously.\n")
                    time.sleep(1)
                    print(self.barbarian.say_dialogue(self.barbarian.dialogue[0]), "\n")
                    time.sleep(1)
                    print(f"{self.player.name}:\n I need a distraction to get into the city, it's very important.\n")
                    time.sleep(2)
                    print(self.barbarian.say_dialogue(self.barbarian.dialogue[1]), "\n")
                    time.sleep(2)
                    print(self.barbarian.say_dialogue(self.barbarian.dialogue[2]), "\n")
                    time.sleep(2)
                    # Player decides whether to strike a deal with the barbarians
                    deal_option = input("Do you want to strike a deal with the barbarian?\n"
                                        "1) Yes, what could go wrong?\n"
                                        "2) Hell no!\n")

                    if deal_option == "1":
                        # Player agrees to the deal
                        print("\n")
                        print(self.barbarian.say_dialogue(self.barbarian.dialogue[3]), "\n")
                        time.sleep(1)
                        print(self.barbarian.say_dialogue(self.barbarian.dialogue[4]), "\n")
                        time.sleep(1)
                        self.__deal_made = True
                        self.add_clue(self.barbarian.clue())
                    elif deal_option == "2":
                        # Player declines the deal
                        print("\n")
                        print(self.barbarian.say_dialogue(self.barbarian.dialogue[5]), "\n")
                        time.sleep(1)

                    self.__barbarians_asked = True

                elif approach_barbarians == "2":
                    # Player decides not to approach the barbarians
                    print("You decide not to approach the barbarians and look for alternative options.\n")
                    time.sleep(1)

            elif barbarian_option == "2":
                # Player decides to return to the previous options
                print("You decide to return to the previous options.\n")
                time.sleep(1)

            else:
                # Invalid option
                print("Invalid option.\n")

        else:
            # If the player has interacted with the barbarians
            barbarian_option = input("1) Return to the barbarians\n"

                                     "2) Return to the previous options\n")
            # If a deal has been made with the barbarians
            if self.__deal_made:
                # If the player chooses to return to the barbarians and the deal is not complete
                if barbarian_option == "1" and not self.__deal_complete:
                    print(self.barbarian.say_dialogue(self.barbarian.dialogue[6]), "\n")
                    time.sleep(1)
                    # If the player has the prized dagger in their inventory
                    if "Prized Dagger" in self.player.inventory:
                        print(f"{self.player.name}:\n Yes, I have it. Can you create a distraction for me?\n")
                        time.sleep(1)
                        print("You give him his prized dagger.\n")
                        time.sleep(2)
                        print(self.barbarian.say_dialogue(self.barbarian.dialogue[7]), "\n")
                        time.sleep(1)
                        print(f"{self.player.name}:\n That wasn't the deal.\n")
                        time.sleep(1)
                        print(self.barbarian.say_dialogue(self.barbarian.dialogue[8]), "\n")
                        time.sleep(2)
                        print("They all reply in unison: No!\n")
                        time.sleep(1)
                        # If the player has enough coins to bribe the barbarians for a distraction
                        if self.player.coins >= 30:
                            print(f"You have {self.player.coins} coins.\n")
                            distraction = input(
                                "Do you wish to give the barbarians some coin(30) to create the distraction?\n"
                                "1) Yes\n"
                                "2) No:\n")
                            if distraction == "1":
                                print(f"{self.player.name}:\n Fine, I do really need to get in there.\n")
                                time.sleep(1)
                                print(self.barbarian.say_dialogue(self.barbarian.dialogue[9]), "\n")
                                time.sleep(1)
                                print("They all rush towards the city gates, charging the guards that block the "
                                      "entrance.\n")
                                time.sleep(2)
                                print("With the distraction in place, you slip past the guards and enter the city.\n")
                                time.sleep(2)
                                self.__guard_interacted = True
                                self.current_location = self.sublocation[5]
                                self.player.coins -= 30
                            elif distraction == "2":
                                print(f"{self.player.name}:\n Forget it then. I'll find my own way in.\n")
                                time.sleep(1)
                                print(self.barbarian.say_dialogue(self.barbarian.dialogue[10]), "\n")
                                time.sleep(1)
                                print("You hear them all cackling as you walk away.\n")
                                time.sleep(1)
                                self.__deal_complete = True
                        else:
                            print("You don't have enough coins to bribe the barbarians.")
                            print("You decide to explore other options.\n")
                            time.sleep(1)
                    else:
                        print(self.barbarian.say_dialogue(self.barbarian.dialogue[11]), "\n")
                        time.sleep(1)

                # If the player chooses to return to the barbarians but the deal is complete
                elif barbarian_option == "1" and self.__deal_complete:
                    print("You got scammed by the barbarians and made a fool of. You decide not to go back to them.\n")
                    time.sleep(2)

                # If the player chooses to return to the previous options
                elif barbarian_option == "2":
                    print("You decide to return to the previous options.\n")
                    time.sleep(1)

                # If the player provides an invalid option
                else:
                    print("Invalid option.\n")
            else:
                # If the player hasn't made a deal with the barbarians yet
                print(self.barbarian.say_dialogue(self.barbarian.dialogue[12]), "\n")
                time.sleep(1)
                deal_option = input("1) Yes, what could go wrong?\n"
                                    "2) Hell no!\n")
                if deal_option == "1":
                    # Player agrees to the deal
                    print("\n")
                    print(self.barbarian.say_dialogue(self.barbarian.dialogue[13]), "\n")
                    time.sleep(1)
                    print(self.barbarian.say_dialogue(self.barbarian.dialogue[14]), "\n")
                    time.sleep(1)
                    self.__deal_made = True
                    self.add_clue(self.barbarian.clue())
                elif deal_option == "2":
                    # Player declines the deal
                    print("\n")
                    print(self.barbarian.say_dialogue
                          (self.barbarian.dialogue[15]), "\n")
                    time.sleep(1)

    def dark_alley(self):
        # Inform the player that they are deciding to investigate the dark alley
        print("You decide to investigate the dark alley.\n")

        # Check if the current location is not already visited
        if self.current_location not in self.visited_sublocations:
            print("As you enter the narrow alley, you hear a faint sound.\n")
            self.visited(self.sublocation[2])

        # Continue the loop as long as the player is in the dark alley
        while self.current_location == self.sublocation[2]:
            # Player chooses an option related to events in the dark alley
            event_result = input("1) Follow the sound\n"
                                 "2) Go deeper into the alley\n"
                                 "3) Leave the alley\n")

            if event_result == "1":
                # If the player chooses to follow the sound
                if not self.__dark_alley_investigated:
                    print("You follow the sound and discover a hidden door.\n")
                    time.sleep(1)
                    print("Behind the door, you find a group of hooded figures planning a secret meeting.\n")
                    time.sleep(2)
                    print("They are dressed in red, blue, and yellow robes.\n")
                    time.sleep(1)
                    print("They almost notice you, but you were able to slip away before they caught you.\n")
                    time.sleep(2)

                    # Add clues based on the discovered information
                    self.add_clue("secret meeting under city")
                    self.add_clue("figures in blue, red, and yellow robes")
                    self.__dark_alley_investigated = True
                else:
                    print("You don't want to go back there; they might see you.\n")
                    time.sleep(1)

            elif event_result == "2":
                # If the player chooses to go deeper into the alley
                if not self.puzzle_complete:
                    print("You find a pile of colored slabs and 3 slots that they seem to fit into.\n")
                    time.sleep(2)

                    # Create an instance of the ColoredSlabPuzzle and play the puzzle
                    colored_slab_puzzle = ColoredSlabPuzzle(self.review_clues())
                    city_pass = colored_slab_puzzle.play_puzzle()

                    # If the puzzle is successfully completed, add the city pass to the player's inventory
                    if city_pass:
                        self.player.add_item(city_pass)
                        self.player.show_inventory()
                    self.puzzle_complete = True
                else:
                    print("You've already completed the puzzle in this area.\n")
                    time.sleep(1)

            elif event_result == "3":
                # If the player chooses to leave the dark alley
                print("You decide to leave the dark alley.")
                time.sleep(1)
                self.current_location = self.sublocation[4]
                break

            else:
                # If the player provides an invalid option
                print("Invalid option.\n")

    def summary(self):
        print("\n==================== Level 2 Player Summary ====================")
        # PLAYER NAME DISPLAY
        print(f"Player Name: {self.player.name}")
        # PLAYER FINAL LEVEL COINS
        print(f"Player Coins: {self.player.coins} coins")
        # PLAYER FINAL CLUES
        print(f"\nClues found in this level: {self.review_clues()}")
        # PLACES VISITED
        print(f"You visited: {self.visited_sublocations}")

        print("==================== End of Player Summary ====================\n")
        self.music_stop()


if __name__ == "__main__":
    # Create a player instance with the name "Player Name"
    player = Player("Player Name")

    # Create a Level2 instance, representing the second level of the game, and pass the player instance to it
    level2 = Level2(player)

    # Start the game from the outside city location
    level2.outside_city()
